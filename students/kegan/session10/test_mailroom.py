"""
Kathryn Egan
"""
import pytest
import io
from MailroomTools import Donor, DonorList


##### DONOR TESTS #####


def test_donor_init():
    d1 = Donor('Helena', 0, 1, 2)
    assert d1.name == 'Helena'
    assert d1.donations == [1, 2]
    d2 = Donor('Bruno', 90)
    assert d2.donations == [90]
    with pytest.raises(ValueError):
        Donor('Raffi')
    with pytest.raises(ValueError):
        Donor('Quenton', 'twenty')
    d3 = Donor('Frank', 'twenty', 20)
    assert d3.donations == [20]


def test_intake_donations():
    assert Donor.intake_donations(500) == [500]
    assert Donor.intake_donations(300, 12) == [300, 12]
    assert Donor.intake_donations(4, 400.83, 5.44) == [4, 400.83, 5.44]
    assert Donor.intake_donations(0) == []


def test_clean_name():
    assert Donor.clean_name('  jim     bob    ') == 'Jim Bob'
    assert Donor.clean_name(
        ' timmy   "C-3P  O" smith') == 'Timmy "C-3P O" Smith'


def test_name():
    d = Donor('Greta', 10)
    d.name = 'Gretta'
    assert d.name == 'Gretta'


def test_donor_str():
    d1 = Donor('Alice', 500)
    assert str(d1) == 'Alice: $500.00'
    d2 = Donor('Beth', 25, 38.5)
    assert str(d2) == 'Beth: $25.00, $38.50'
    d3 = Donor('Chris', .42424242)
    assert str(d3) == 'Chris: $0.42'


def test_donor_repr():
    d1 = Donor('Alice', 500)
    assert repr(d1) == 'Donor("Alice", 500.0)'
    d2 = Donor('Beth', 25, 38.5)
    assert repr(d2) == 'Donor("Beth", 25.0, 38.5)'
    d3 = Donor('Chris', .42424242)
    assert repr(d3) == 'Donor("Chris", 0.42424242)'


def test_donor_equals():
    d1 = Donor('Alice', 500)
    d2 = Donor('Annie', 1000)
    d3 = Donor('Annie', 1000)
    d4 = Donor('Alice', 20)
    assert d2 == d3
    assert d1 != d3
    assert d1 != d4


def test_donor_lt():
    d1 = Donor('Alice', 500)
    d2 = Donor('Barbara', 1000)
    d3 = Donor('Connie', 2000)
    assert d1 < d2
    assert d2 <= d3
    assert d3 > d1
    assert d3 >= d3
    d4 = Donor('Connie', 5000)
    assert d4 > d3


def test_donor_contains():
    d1 = Donor('Ali', 20, 50, 100)
    assert 20 in d1
    assert 25 not in d1


def test_donor_thank_you():
    d1 = Donor('Benedict Cumberbatch', 200000.0)
    assert (
        d1.thank(all_donations=True) ==
        'Dear Benedict Cumberbatch,\nThank you for your generous gift of ' +
        '$200,000.00. Your donation will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')
    assert (
        d1.thank() ==
        'Dear Benedict Cumberbatch,\nThank you for your generous gift of ' +
        '$200,000.00. Your donation will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')

    d2 = Donor('Elon Musk', 10000.0, 150000.0, 100000.0)
    assert (
        d2.thank(all_donations=True) ==
        'Dear Elon Musk,\nThank you for your generous gifts of ' +
        '$10,000.00, $150,000.00 and $100,000.00. Your donations, totalling an ' +
        'incredible $260,000.00, will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')
    assert (
        d2.thank() ==
        'Dear Elon Musk,\nThank you for your generous gift of ' +
        '$100,000.00. Your donation will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')

    d3 = Donor('Dad', 20.0, 5.0)
    assert (
        d3.thank(all_donations=True) ==
        'Dear Dad,\nThank you for your generous gifts of ' +
        '$20.00 and $5.00. Your donations, totalling $25.00, will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')
    assert (
        d3.thank() ==
        'Dear Dad,\nThank you for your generous gift of ' +
        '$5.00. Your donation will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')

    d4 = Donor('Donald Trump', 2.81)
    assert (
        d4.thank(all_donations=True) ==
        'Dear Donald Trump,\nThank you for your generous gift of ' +
        '$2.81. Your donation will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')
    assert (
        d4.thank() ==
        'Dear Donald Trump,\nThank you for your generous gift of ' +
        '$2.81. Your donation will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')

    d5 = Donor('Billy Neighbor', .54, .01, .25)
    assert (
        d5.thank(all_donations=True) ==
        'Dear Billy Neighbor,\nThank you for your generous gifts of ' +
        '$0.54, $0.01 and $0.25. Your donations, totalling $0.80, will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')
    assert (
        d5.thank() ==
        'Dear Billy Neighbor,\nThank you for your generous gift of ' +
        '$0.25. Your donation will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')


def test_donor_add():
    d = Donor('Quincy', 10)
    d.add(50)
    assert d.donations == [10, 50]
    d.add(200, 400)
    assert d.donations == [10, 50, 200, 400]



##### DONORLIST TESTS #####


d1 = Donor('Abigail', 50)
d2 = Donor('Berta', 100, 10)
d3 = Donor('Carla', 600.59)


def test_donorlist():
    l1 = DonorList()
    assert l1.donors == []
    l2 = DonorList(d1, d2)
    assert l2.donors == [d1, d2]
    ds = [d1, d2]
    l3 = DonorList(*ds)
    assert l3.donors == ds


def test_donorlist_contains():
    l1 = DonorList(d1, d2)
    assert d1 in l1
    assert d3 not in l1
    assert 'Abigail' in l1
    assert 'Frankie' not in l1
    d4 = Donor('Abigail', 200)
    d5 = Donor('Annie', 50)
    assert d4 not in l1
    assert d5 not in l1


def test_donor_names():
    l1 = DonorList(d3, d1, d2)
    assert l1.donor_names == ['Carla', 'Abigail', 'Berta']


def test_donorlist_get():
    l1 = DonorList(d1, d2, d3)
    assert l1['Abigail'] == d1
    with pytest.raises(KeyError):
        l1['Dirk']


def test_donorlist_update():
    l1 = DonorList(d1, d2, d3)
    l1.update(Donor('Abigail', 100))
    assert Donor('Abigail', 50, 100) in l1
    assert Donor('Abigail', 100) not in l1
    assert Donor('Abigail', 50) not in l1
    l1.update(Donor('Steve', 25))
    assert Donor('Steve', 25) in l1


def test_sort_by():
    d1 = Donor('Alice', 200, 200)
    d2 = Donor('Bill', 100, 100, 100, 100, 100)
    l1 = DonorList(d1, d2)
    assert l1.sort_by('total') == [d2, d1]
    assert l1.sort_by('total', low_to_high=True) == [d1, d2]
    assert l1.sort_by('average') == [d1, d2]
    assert l1.sort_by('average', low_to_high=True) == [d2, d1]
    assert l1.sort_by('num') == [d2, d1]
    assert l1.sort_by('num', low_to_high=True) == [d1, d2]
    with pytest.raises(KeyError):
        l1.sort_by('foo')


def test_from_dictionary():
    donors = {
        'Benedict Cumberbatch': [200000.0],
        'Elon Musk': [10000.0, 150000.0, 100000.0]}
    l1 = DonorList.from_dictionary(donors)
    assert 'Benedict Cumberbatch' in l1
    assert l1['Elon Musk'] == Donor('Elon Musk', 10000.0, 150000.0, 100000.0)


def test_report_dollar():
    assert DonorList.dollar(1001010101010, 5) == '$999,999.99+'
    assert DonorList.dollar(50, 10) == '$    50.00'
    assert DonorList.dollar(20.35032, 7) == '$ 20.35'


def test_report_name():
    assert (
        DonorList.name('Her Royal Majesty Queen Elizabeth', 10) ==
        'Her Ro... ')
    assert DonorList.name('Bob', 10) == 'Bob       '


def test_report_number():
    assert DonorList.number(1001010101010, 5) == '999,999+ '
    assert DonorList.number(500, 6) == '    500 '


def test_write_to():
    f1 = io.StringIO()
    d1 = Donor('Agatha Smith', 200000.0)
    d2 = Donor('Brett Taylor', 100.0, 150.0, 89.90)
    l1 = DonorList(d1, d2)
    l1.write_to(f1)
    csv = f1.getvalue()
    assert (
        csv ==
        'Agatha Smith,200000.00\n' +
        'Brett Taylor,100.00,150.00,89.90\n')
    l2 = DonorList()
    f2 = io.StringIO()
    l2.write_to(f2)
    csv = f2.getvalue()
    assert csv == ''


# def test_create_report():
#     d1 = Donor('Benedict Cumberbatch', 200000.0)
#     d2 = Donor('Elon Musk', 10000.0, 150000.0, 100000.0)
#     d3 = Donor('Dad', 20.0, 5.0)
#     d4 = Donor('Donald Trump', 2.81)
#     d5 = Donor('Billy Neighbor', .54, .01, .25)
#     d6 = Donor(
#         'Daenerys Stormborn of the House Targaryen, ' +
#         'First of Her Name, the Unburnt, ' +
#         'Queen of the Andals and the First Men, ' +
#         'Khaleesi of the Great Grass Sea, Breaker of Chains, ' +
#         'and Mother of Dragons', *[100] * 10000000)
#     d7 = Donor('Eazy-E', 1000000000000000)
#     donors = DonorList(d1, d2, d3, d4, d5, d6, d7)
#     report = donors.report()
#     assert (
#         report ==
#         'Donor Name          | Total Given | Num Gifts | Average Gift \n' +
#         '------------------------------------------------------------\n' +
#         'Eazy-E               $999,999.99+           1  $ 999,999.99+\n' +
#         'Daenerys Stormbo...  $999,999.99+    999,999+  $      100.00\n' +
#         'Elon Musk            $ 260,000.00           3  $   86,666.67\n' +
#         'Benedict Cumberbatch $ 200,000.00           1  $  200,000.00\n' +
#         'Dad                  $      25.00           2  $       12.50\n' +
#         'Donald Trump         $       2.81           1  $        2.81\n' +
#         'Billy Neighbor       $       0.80           3  $        0.27')


def test_create_report2():
    l1 = DonorList()
    r1 = l1.report()
    assert (
        r1 ==
        'Donor Name          | Total Given | Num Gifts | Average Gift \n' +
        '------------------------------------------------------------')


def test_multiply_no_min_max():
    d1 = Donor('Helga', 5, 10, 15)
    assert (
        d1.multiply(2, min_donation=0, max_donation=100000000) ==
        Donor('Helga', 10, 20, 30))
    assert (
        d1.multiply(3, min_donation=0, max_donation=100000000) ==
        Donor('Helga', 15, 30, 45))
    assert (
        d1.multiply(4, min_donation=0, max_donation=100000000) ==
        Donor('Helga', 20, 40, 60))


def test_multiply_min():
    d1 = Donor('Helga', 5, 10, 15)
    assert d1.multiply(
        2, min_donation=6, max_donation=1000) == Donor('Helga', 5, 20, 30)


def test_multiply_max():
    d1 = Donor('Helga', 5, 10, 15)
    assert d1.multiply(
        2, min_donation=0, max_donation=12) == Donor('Helga', 10, 20, 15)


def test_multiply_min_max():
    d1 = Donor('Helga', 5, 10, 15)
    assert d1.multiply(
        3, min_donation=7, max_donation=12) == Donor('Helga', 5, 30, 15)


def test_challenge_donor():
    l1 = DonorList(Donor('Chester', 5, 12, 3), Donor('Buster', 6, 6, 4))
    assert (
        l1.challenge_donor('Chester', 2, min_donation=4, max_donation=6) ==
        Donor('Chester', 10, 12, 3))
    assert (
        l1.challenge_donor('Buster', 2, min_donation=6, max_donation=6) ==
        Donor('Buster', 12, 12, 4))


def test_challenge_all():
    l1 = DonorList(Donor('Chester', 5, 12, 3), Donor('Buster', 6, 6, 4))
    l2 = l1.challenge_all(2, min_donation=10)
    assert Donor('Chester', 5, 24, 3) in l2
    assert Donor('Buster', 6, 6, 4) in l2

