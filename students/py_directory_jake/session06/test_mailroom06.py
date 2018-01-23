"""Mailroom v6 Unit Tests"""
import pytest

TEST1 = [('John Booth', 50,'\nThank you! John Booth has donated $50 to a great cause!\n'),
		('Eric Johnson', 60,'\nThank you! Eric Johnson has donated $60 to a great cause!\n'),
		('Maria Volk', 700,'\nThank you! Maria Volk has donated $700 to a great cause!\n'),
		('Wes Anderson', 900,'\nThank you! Wes Anderson has donated $900 to a great cause!\n'),
		('Roberto Valdo', 700,'\nThank you! Roberto Valdo has donated $700 to a great cause!\n')]

TEST2 = [('John Booth', 20000, 2, 's','\nDear John Booth,\n\nThank you for your very kind donation of 20000 over 2 donations.\nYour generiosity has been put to very good use.\n\nSincerely,\nThe Team'),
		('Eric Johnson', 60000, 1, '','\nDear Eric Johnson,\n\nThank you for your very kind donation of 60000 over 1 donation.\nYour generiosity has been put to very good use.\n\nSincerely,\nThe Team'),
		('Maria Volk', 5500, 3, 's','\nDear Maria Volk,\n\nThank you for your very kind donation of 5500 over 3 donations.\nYour generiosity has been put to very good use.\n\nSincerely,\nThe Team'),
		('Wes Anderson', 23500, 5, 's','\nDear Wes Anderson,\n\nThank you for your very kind donation of 23500 over 5 donations.\nYour generiosity has been put to very good use.\n\nSincerely,\nThe Team'),
		('Roberto Valdo', 10, 1, '','\nDear Roberto Valdo,\n\nThank you for your very kind donation of 10 over 1 donation.\nYour generiosity has been put to very good use.\n\nSincerely,\nThe Team')]
    
TEST3 = [('John Booth',20000, True),
		('Eric Johnson',60000, True),
		('Maria Volk',5500,True),
		('Wes Anderson',23500, True),
		('Roberto Valdo',10, True)]

#-----------------------------------------------------------------
# TEST - Send a Thank You
#-----------------------------------------------------------------

@pytest.mark.parametrize('parm1,parm2,result',TEST1)
def test_send_thank_you(parm1,parm2,result):
	from mailroom_session06 import send_thank_you
	assert send_thank_you(parm1,parm2) == result


def test_check_dict():
	from mailroom_session06 import check_dict
	assert check_dict

def test_quit():
	from mailroom_session06 import quit
	assert quit

#-----------------------------------------------------------------
# TEST - Add Donor and Amount
#-----------------------------------------------------------------

@pytest.mark.parametrize('parm1,parm2,result', TEST3)
def test_add_donation(parm1, parm2, result):
	from mailroom_session06 import add_donation
	assert add_donation(parm1, parm2) == result


#-----------------------------------------------------------------
# TEST - Send Letters to Everyone
#-----------------------------------------------------------------

@pytest.mark.parametrize('parm1,parm2,parm3,parm4,result',TEST2)
def test_letter_output(parm1,parm2,parm3,parm4,result):
	from mailroom_session06 import letter_output
	assert letter_output(parm1,parm2,parm3,parm4) == result
	

