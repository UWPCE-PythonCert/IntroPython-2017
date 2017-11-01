"""
Kathryn Egan
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('course')
parser.add_argument('name', help='name of student')
parser.add_argument('grade', help='student grade', type=float)
parser.add_argument('--nickname', '-n', help='student nickname (optional)')
parser.add_argument(
    '--grad', '-g', action='store_true', help='graduate student (optional)')

args = parser.parse_args()

nickname = ', aka {},'.format(args.nickname) if args.nickname else ''
graduate = ' (graduate level)' if args.grad else ''
output = "{}{} received a {:.1f} in {}{}.".format(
    args.name.title(), nickname, args.grade, args.course, graduate)
print(output)
