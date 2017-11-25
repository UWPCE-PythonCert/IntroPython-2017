#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Module to clone and update (pull) repositories at a GitHub organization
site to local repository directories.  Connects to GitHub as the current
user.  Private repositories can be seen and cloned/updated if appropriate
conditions are met.

This package was developed at [redacted] inspired by Kenneth Reitz's GitHub Syncer.

[NOTE: the oroginal is a more pythonic script....]

'''

from __future__ import print_function

import sys
import os
import os.path

from datetime import datetime
import json
import re
import subprocess
import traceback
# import urllib.request as urllib2
import requests

class GHOrgSync(object):
    '''
    Class to clone and update (pull) repositories at an origanization's
    GitHub site to local repository directories.  Connects to GitHub
    as the current user.

    If the environment variable GITUSERTOKEN is given and its value
    is not blank, authentication is added to the requests for repository
    information using this value as the personal access token.  If
    successful, information about both private and public repositories
    will be obtained.  If the GITUSERTOKEN environment variable is not
    given or its value is blank, only information about public repositories
    will be obtained.

    Uses SSH URLs (i.e., git@github.com/...) to clone the repositories.
    In order to clone private repositories, the current user's GitHub
    account must be configured with the user's SSH key.

    See:
        https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
        https://help.github.com/articles/connecting-to-github-with-ssh/
    '''

    def __init__(self, orgname, localdir, nameregex=r'[\w\.-]+'):
        '''
        Clone and update (pull) acceptable repositories at the given
        GitHub organization site under the given local directory.

        Arguments:
            orgname   : (str) GitHub organization name (e.g., '/UWPCE-PythonCert')
            localdir  : (str) local directory under which the repositories
                              will be, or are already, cloned
            nameregex : (str) regular expression to use for checking
                              acceptable repository names; r'[\w\.-]+' allows
                              one or more alphanumeric, underscore, period,
                              and dash characters
        '''
        self.__orgname = orgname;
        self.__localdir = localdir
        self.__nameregex = nameregex

    def getrepos(self):
        '''
        Returns a list of information about GitHub repositories associated
        with the organization specified by this instance.

        If the environment variable GITUSERTOKEN is given and its value
        is not blank, authentication is added to the requests for repository
        information using this value as the personal access token.  If
        successful, information about both private and public repositories
        will be returned.  If the GITUSERTOKEN environment variable is not
        given or its value is blank, only information about public repositories
        will be returned.

        Checks that the repository name matches the name regular expression.
        Also checks the SSH URL is the expected URL for the organization and
        repository name.  An error message is printed to sys.stderr about any
        repositories that were ignored.

        Each entry is the list returned is a dictionary with key-value pairs:
            'name'      : (str) repository name
            'private'   : (bool) is this a private repository?
            'sshurl'    : (str) SSH URL of the repository; e.g.,
                                git@github.com:UWPCE-PythonCert/IntroPython-2017.git
            'parenturl' : (str) SSH URL of the parent GitHub repository, or
                                an empty string if this repository is not
                                a fork of another GitHub repository
        '''
        repos = [ ]
        # regex to check the URL
        urlregex = re.compile('git@github.com:{org}/({regex}).git'.format(
                               org=self.__orgname, regex=self.__nameregex))
        # authentication information
        try:
            token = os.getenv('GITUSERTOKEN', '').strip()
        except Exception: # multiiple things wrong here!
            token = ''
        # Get the info about all the repos at the organization that can be seen.
        print("about to make request for allrepos")
        # reposreq = urllib2.Request('https://api.github.com/orgs/{org}/repos?page={pnum}'.format(
        #                             org=self.__orgname, pnum=pagenum))
        conn = requests.get('https://api.github.com/orgs/{org}/repos'.format(org=self.__orgname))
        # if token:
        #     print("adding auth token")
        #     reposreq.add_header('Authorization', 'token ' + token)
        #conn = urllib2.urlopen(reposreq)
        print("request returned")
        repolist = conn.json()
        if "message" in repolist:
            print("something went wrong with API. Message:", repolist["message"])
            raise RuntimeError
        print(repolist)
        conn.close()
        for repo in repolist:
            print("repo::", repo)
            name = str(repo[u'name'])
            private = bool(repo[u'private'])
            sshurl = str(repo[u'ssh_url'])
            match = urlregex.match(sshurl)
            if match and (match.group(1) == name):
                if bool(repo[u'fork']):
                    # inforeq = urllib2.Request('https://api.github.com/repos/{org}/{rname}'.format(
                    #                            org=self.__orgname, rname=name))
                    conn = requests.get('https://api.github.com/repos/{org}/{rname}'.format(
                                               org=self.__orgname, rname=name))
                    # if token:
                    #     inforeq.add_header('Authorization', 'token ' + token)
                    # conn = urllib2.urlopen(inforeq)
                    #repoinfo = json.load(conn)
                    repoinfo = conn.json()
                    conn.close()
                    parenturl = str(repoinfo[u'parent'][u'ssh_url'])
                else:
                    parenturl = ''
                repos.append({'name': name,
                              'private': private,
                              'sshurl': sshurl,
                              'parenturl': parenturl})
            else:
                timestamp = datetime.today().isoformat(' ')
                if not match:
                    explanation = 'no match'
                else:
                    explanation = 'mismatch'
                print('{ts} :: repo ignored ({expl}) {rname} : {url}'.format(
                      ts=timestamp, expl=explanation, rname=name, url=sshurl), file=sys.stderr)
        return repos

    def syncrepo(self, repo):
        '''
        Create or update (pull) a local clone of the given repository.
        If a problem occurs, a message is printed to sys.stderr

        Arguments:
            repo : (dict) repository information dictionary with key-value pairs:
                'name'      : (str) repository name; e.g., PyFerret
                'private'   : (bool) is this a private repository?
                'sshurl'    : (str) SSH URL of the repository; e.g.,
                                    git@github.com:UWPCE-PythonCert/IntroPython-2017.git
                'parenturl' : (str) SSH URL of the parent GitHub repository to set
                                    as the upstream repository when creating the
                                    local clone.  If empty or None, or if the local
                                    clone already exists, this value is ignored.
        Returns: (bool) if successful
        '''
        # Get the info about the repo
        name = repo['name']
        private = repo['private']
        sshurl = repo['sshurl']
        parenturl = repo['parenturl']
        # Get the local clone location for this repo
        if private:
            basedir = os.path.join(self.__localdir, 'private')
        else:
            basedir = os.path.join(self.__localdir, 'public')
        clonedir = os.path.join(basedir, name)
        # Deal with this repo
        if not os.path.exists(clonedir):
            # New repo - clone it
            os.chdir(basedir)
            retval = subprocess.call(['git', 'clone', '--quiet', sshurl])
            if retval != 0:
                timestamp = datetime.today().isoformat(' ')
                print('{ts} :: cannot clone repository {rname} : {url}'.format(
                       ts=timestamp, rname=name, url=sshurl), file=sys.stderr)
                return False
            if parenturl:
                # Fork - record its upstream
                os.chdir(clonedir)
                retval = subprocess.call(['git', 'remote', 'add', 'upstream', parenturl])
                if retval != 0:
                    timestamp = datetime.today().isoformat(' ')
                    print('{ts} :: cannot add to {rname} the upstream {url}'.format(
                           ts=timestamp, rname=name, url=parenturl), file=sys.stderr)
                    return False
        elif os.path.isdir(clonedir):
            # Verify it is a git repo
            dotgit = os.path.join(clonedir, '.git')
            if os.path.isdir(dotgit):
                # Existing local clone - update it (pull)
                os.chdir(clonedir)
                retval = subprocess.call(['git', 'pull', '--quiet'])
                if retval != 0:
                    timestamp = datetime.today().isoformat(' ')
                    print('{ts} :: cannot update (pull) repository {rname}'.format(
                           ts=timestamp, rname=name), file=sys.stderr)
                    return False
            else:
                timestamp = datetime.today().isoformat(' ')
                print('{ts} :: not a git repository: {dname}'.format(
                       ts=timestamp, dname=clonedir), file=sys.stderr)
                return False
        else:
            # Not a directory
            timestamp = datetime.today().isoformat(' ')
            print('{ts} :: not a directory: {dname}'.format(
                   ts=timestamp, dname=clonedir), file=sys.stderr)
            return False
        return True


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("\n" + \
              "Clones and updates (pulls) repositories at an organization's GitHub site\n" + \
              "under a local directory.\n" + \
              "\n" + \
              "    Usage:  {0}  orgname  localdir\n".format(sys.argv[0]) + \
              "    where:\n" + \
              "        orgname   is the GitHub organization name (e.g., /UWPCE-PythonCert)\n" + \
              "        localdir  is the full-path of the directory containing a 'private'\n" + \
              "                  and a 'public' subdirectory which will contain the cloned\n" + \
              "                  private and public, respectively, repository subdirectories\n" + \
              "\n", file=sys.stderr)
        sys.exit(1)
    orgname = sys.argv[1]
    localdir = sys.argv[2]
    retval = 0
    try:
        cloner = GHOrgSync(orgname, localdir)
        repos = cloner.getrepos()
        for repo in repos:
            print(repo['name'])
        if len(repos) < 1:
            timestamp = datetime.today().isoformat(' ')
            print('{ts} :: no repositories found for {site}'.format(ts=timestamp, site=orgname), file=sys.stderr)
            sys.exit(2)
        for repoinfo in repos:
            if not cloner.syncrepo(repoinfo):
                retval = 3
    except Exception:
        traceback.print_exc()
        sys.exit(-1)
    sys.exit(retval)

