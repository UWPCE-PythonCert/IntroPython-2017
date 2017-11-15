"""
Kathryn Egan
"""
from mailroom import *


def test_get_thank_you():
    assert (
        get_thank_you('Benedict Cumberbatch', [200000.0]) ==
        'Dear Benedict Cumberbatch,\nThank you for your generous gift of ' +
        '$200,000. Your donation will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')

    assert(
        get_thank_you('Elon Musk', [10000.0, 150000.0, 100000.0]) ==
        'Dear Elon Musk,\nThank you for your generous gifts of ' +
        '$10,000, $150,000 and $100,000. Your donations, totalling an ' +
        'incredible $260,000, will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')

    assert (
        get_thank_you('Dad', [20.0, 5.0]) ==
        'Dear Dad,\nThank you for your generous gifts of ' +
        '$20 and $5. Your donations, totalling $25, will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')

    assert (
        get_thank_you('Donald Trump', [2.81]) ==
        'Dear Donald Trump,\nThank you for your generous gift of ' +
        '$2.81. Your donation will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')

    assert (
        get_thank_you('Billy Neighbor', [.54, .01, .25]) ==
        'Dear Billy Neighbor,\nThank you for your generous gifts of ' +
        '$0.54, $0.01 and $0.25. Your donations, totalling $0.80, will ' +
        'go towards feeding homeless kittens in Seattle. ' +
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care')


def test_dollar():
    assert dollar(5) == '$5'
    assert dollar(0) == '$0'
    assert dollar(.01) == '$0.01'
    assert dollar(2000000) == '$2,000,000'
    assert dollar(1234.56) == '$1,234.56'


def test_format_name():
    assert format_name('Joe', 5) == 'Joe   '
    assert format_name('Billy Bob Thornton', 8) == 'Billy... '


def test_format_dollar():
    assert format_dollar(666, 8) == '$  666.00'
    assert format_dollar(100000000, 12) == '$999,999.99+'


def test_format_number():
    assert format_number(25, 5) == '     25 '
    assert format_number(100000000000000, 8) == '  999,999+ '


def test_create_report():
    assert (
        create_report() == 
        'Donor Name           | Total Given | Num Gifts | Average Gift\n' +
        '-------------------------------------------------------------\n' +
        'Daenerys Stormbor...  $999,999.99+    999,999+  $      100.00\n' +
        'Elon Musk             $ 260,000.00           3  $   86,666.67\n' +
        'Benedict Cumberbatch  $ 200,000.00           1  $  200,000.00\n' +
        'Dad                   $      25.00           2  $       12.50\n' +
        'Donald Trump          $       2.81           1  $        2.81\n' +
        'Billy Neighbor        $       0.80           3  $        0.27')
