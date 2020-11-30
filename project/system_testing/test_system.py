# WARNING. It is an autogenerated file, don't change it manually.
import logging
from pathlib import Path

import pytest
from mahjong.tile import TilesConverter
from reproducer import TenhouLogReproducer, parse_reproducer_args

logger = logging.getLogger()
system_testing_folder = Path(__file__).parent.absolute()


def _run_reproducer(file_name, reproducer_command):
    log_file_path = system_testing_folder / "fixtures" / file_name
    opts = parse_reproducer_args(reproducer_command.replace("python ", "").split(" "))
    reproducer = TenhouLogReproducer(log_id=None, file_path=log_file_path, logger=logger)
    return reproducer.reproduce(opts.player, opts.wind, opts.honba, opts.tile, opts.action, opts.n)


def test_system_case_1():
    """
    Case #1
    Bot discarded 2s by suji because of 2 additional ukeire in ryanshanten, instead of discarding the safe tile.
    """

    reproducer_command = "python reproducer.py --log 2020102200gm-0001-7994-1143916f --player 0 --wind 2 --honba 3 --tile=1s --n 2 --action=draw"
    allowed_discards = ["3s", "5s"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("1.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_2():
    """
    Case #2
    6m and 8m have equal ukeire, but 6m is safe.
    """

    reproducer_command = "python reproducer.py --log 2020102204gm-0001-7994-fb636348 --player 3 --wind 7 --honba 0  --action=draw --tile=6z"
    allowed_discards = ["6m", "3s"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("2.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_3():
    """
    Case #3
    It was a bad meld. We don't want to open hand here.
    """

    reproducer_command = "python reproducer.py --log 2020102208gm-0009-0000-40337c9c --player Xenia --wind 3 --honba 0  --action enemy_discard --tile 1s"
    needed_meld = None
    tile_after_meld = None

    result_meld, result_tile_after_meld = _run_reproducer("3.txt", reproducer_command)
    assert result_meld == needed_meld
    assert result_tile_after_meld is None


def test_system_case_4():
    """
    Case #4
    It was a bad meld. We don't want to open hand here.
    """

    reproducer_command = "python reproducer.py --log 2020102208gm-0009-0000-40337c9c --player Xenia --wind 4 --honba 0  --action enemy_discard --tile 5s"
    needed_meld = None
    tile_after_meld = None

    result_meld, result_tile_after_meld = _run_reproducer("4.txt", reproducer_command)
    assert result_meld == needed_meld
    assert result_tile_after_meld is None


def test_system_case_5():
    """
    Case #5
    Riichi dora tanki is a better move here.
    """

    reproducer_command = "python reproducer.py --log 2020102517gm-0009-0000-67fd5f29 --player Xenia --wind 2 --honba 0 --action draw --n 1 --tile 7s"
    allowed_discards = ["1p", "4p"]
    with_riichi = True

    result, with_riichi_result = _run_reproducer("5.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_6():
    """
    Case #6
    Let's defend here.
    """

    reproducer_command = "python reproducer.py --log 2020102602gm-0009-0000-ba58220e --player Kaavi --wind 6 --honba 1 --action draw --n 2 --tile 1s"
    allowed_discards = ["1s"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("6.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_7():
    """
    Case #7
    7p was wrongly detected as dangerous tile, it is not like this
    """

    reproducer_command = "python reproducer.py --log 2020102608gm-0009-0000-ff33fd82 --player Wanjirou --wind 4 --honba 0 --action draw --n 1 --tile 7p"
    allowed_discards = ["7p"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("7.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


@pytest.mark.skip("Need to investigate it.")
def test_system_case_8():
    """
    Case #8
    Honors are dangerous on this late stage of the game. And we have 2 shanten. Let's fold with 6s
    """

    reproducer_command = "python reproducer.py --log 2020102619gm-0089-0000-dfaf5b1d --player Xenia --wind 4 --honba 0 --action draw --n 1 --tile 2m"
    allowed_discards = ["6s"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("8.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_9():
    """
    Case #9
    """

    reproducer_command = "python reproducer.py --log 2020102701gm-0089-0000-8572de24 --player Ichihime --wind 7 --honba 1 --action draw --n 1 --tile 7s"
    allowed_discards = ["3p"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("9.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_10():
    """
    Case #10
    """

    reproducer_command = "python reproducer.py --log 2020102710gm-0009-7994-88f45f2d --player 3 --wind 5 --honba 0 --tile 4m --action enemy_discard"
    needed_meld = None
    tile_after_meld = None

    result_meld, result_tile_after_meld = _run_reproducer("10.txt", reproducer_command)
    assert result_meld == needed_meld
    assert result_tile_after_meld is None


def test_system_case_11():
    """
    Case #11
    There is no need in damaten. Let's riichi.
    """

    reproducer_command = "python reproducer.py --log 2020102720gm-0089-0000-65eb30bf --player Xenia --wind 8 --honba 2 --action draw --n 1 --tile 4m"
    allowed_discards = ["7s"]
    with_riichi = True

    result, with_riichi_result = _run_reproducer("11.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_12():
    """
    Case #12
    Chun is too dangerous to discard.
    """

    reproducer_command = "python reproducer.py --log 2020102721gm-0089-0000-67865130 --player Xenia --wind 5 --honba 0 --action draw --n 1 --tile 4m"
    allowed_discards = ["7s"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("12.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_13():
    """
    Case #13
    Hatsu is too dangerous to discard.
    """

    reproducer_command = "python reproducer.py --log 2020102821gm-0089-0000-49e1d208 --player Ichihime --wind 1 --honba 2 --action draw --n 1 --tile 6z"
    allowed_discards = ["7m"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("13.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_14():
    """
    Case #14
    3p is genbutsu
    """

    reproducer_command = "python reproducer.py --log 2020102908gm-0089-0000-e1512a30 --player Ichihime --wind 7 --honba 0 --action draw --n 2 --tile 6p"
    allowed_discards = ["3p"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("14.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_15():
    """
    Case #15
    5p is too dangerous to discard
    """

    reproducer_command = "python reproducer.py --log 2020102900gm-0089-0000-5cc13112 --player Xenia --wind 2 --honba 2 --tile 5p --n 2 --action draw"
    allowed_discards = ["5s"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("15.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_16():
    """
    Case #16
    We need to fold here
    """

    reproducer_command = "python reproducer.py --log 2020102921gm-0089-0000-764321f0 --player Xenia --wind 1 --honba 0 --action draw --n 1 --tile 3m"
    allowed_discards = ["7s", "3m"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("16.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_17():
    """
    Case #17
    Bad meld for honitsu.
    """

    reproducer_command = "python reproducer.py --log 2020102922gm-0089-0000-d3c4e90b --player Xenia --wind 1 --honba 0 --action enemy_discard --n 1 --tile 8p"
    needed_meld = None
    tile_after_meld = None

    result_meld, result_tile_after_meld = _run_reproducer("17.txt", reproducer_command)
    assert result_meld == needed_meld
    assert result_tile_after_meld is None


def test_system_case_18():
    """
    Case #18
    """

    reproducer_command = "python reproducer.py --log 2020103005gm-0089-0000-01fc4f4d --player Kaavi --wind 3 --honba 0 --action draw --n 3 --tile 6s"
    allowed_discards = ["3p", "6s"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("18.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_19():
    """
    Case #19
    """

    reproducer_command = "python reproducer.py --log 2020111101gm-0009-7994-f22b8c57 --wind 4 --honba 2 --player 2 --tile 8m --action enemy_discard"
    needed_meld = None
    tile_after_meld = None

    result_meld, result_tile_after_meld = _run_reproducer("19.txt", reproducer_command)
    assert result_meld == needed_meld
    assert result_tile_after_meld is None


def test_system_case_20():
    """
    Case #20
    """

    reproducer_command = "python reproducer.py --log 2020111111gm-0009-7994-5550ade1 --wind 8 --honba 1 --player 0 --tile 7z --action enemy_discard"
    needed_meld = {"type": "pon", "tiles": "777z"}
    tile_after_meld = "3p"

    result_meld, result_tile_after_meld = _run_reproducer("20.txt", reproducer_command)
    assert result_meld.type == needed_meld["type"]
    assert TilesConverter.to_one_line_string(result_meld.tiles) == needed_meld["tiles"]
    assert TilesConverter.to_one_line_string([result_tile_after_meld.tile_to_discard_136]) == tile_after_meld


def test_system_case_21():
    """
    Case #21
    """

    reproducer_command = "python reproducer.py --log 2020111401gm-0009-7994-7429e8e0 --wind 1 --honba 1 --action draw --tile 3s --player 3"
    _run_reproducer("21.txt", reproducer_command)


def test_system_case_22():
    """
    Case #22
    """

    reproducer_command = "python reproducer.py --log 2020111402gm-0009-7994-41f6c1a1 --wind 3 --honba 0 --action enemy_discard --tile 5p --player 1"
    _run_reproducer("22.txt", reproducer_command)


def test_system_case_23():
    """
    Case #23
    """

    reproducer_command = (
        "python reproducer.py --file failed_2020-11-11_13_06_26_885.txt --wind 3 --honba 0 --tile 1z --n 2 --player 3"
    )
    _run_reproducer("23.txt", reproducer_command)


def test_system_case_24():
    """
    Case #24
    """

    reproducer_command = "python reproducer.py --file failed_2020-11-11_12_52_06_023.txt --wind 8 --honba 0 --action enemy_discard --tile 3s --player 0"
    _run_reproducer("24.txt", reproducer_command)


def test_system_case_25():
    """
    Case #25
    """

    reproducer_command = (
        "python reproducer.py --file failed_2020-11-11_12_19_20_515.txt --wind 3 --honba 1 --tile 6s --player 2"
    )
    _run_reproducer("25.txt", reproducer_command)


def test_system_case_26():
    """
    Case #26
    """

    reproducer_command = "python reproducer.py --log 2020102620gm-0089-0000-c558d68c --player Kaavi --wind 1 --honba 2 --action draw --n 2 --tile 4p"
    allowed_discards = ["3s", "8p", "3p", "2p"]
    with_riichi = None

    result, with_riichi_result = _run_reproducer("26.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards


def test_system_case_27():
    """
    Case #27
    """

    reproducer_command = "python reproducer.py --log 2020102208gm-0009-0000-1d3d08c8 --player Ichihime --wind 5 --honba 1 --tile 1z --action draw"
    _run_reproducer("27.txt", reproducer_command)


def test_system_case_28():
    """
    Case #28
    """

    reproducer_command = "python reproducer.py --log 2020102008gm-0001-7994-9438a8f4 --player Wanjirou --wind 3 --honba 0 --tile 7p --action enemy_discard"
    needed_meld = None
    tile_after_meld = None

    result_meld, result_tile_after_meld = _run_reproducer("28.txt", reproducer_command)
    assert result_meld == needed_meld
    assert result_tile_after_meld is None


def test_system_case_29():
    """
    Case #29
    There was crash after open kan in the real game.
    """

    reproducer_command = (
        "python reproducer.py --log 2020112003gm-0089-0000-72c1d092 --player Xenia --wind 7 --honba 0 --tile 1s"
    )
    _run_reproducer("29.txt", reproducer_command)


def test_system_case_30():
    """
    Case #30
    We are pushing here, even if it is karaten we still want to keep tempai.
    """

    reproducer_command = "python reproducer.py --log 2020112215gm-0009-0000-9c894eca --player 1 --wind 8 --honba 0 --action draw --n 1 --tile 7m"
    allowed_discards = ["5m"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("30.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_31():
    """
    Case #31
    Regression with honitsu and chinitsu detection
    """

    reproducer_command = "python reproducer.py --log 2020112219gm-0089-0000-8de03653 --player 0 --wind 1 --honba 0 --action draw --n 1 --tile 1s"
    allowed_discards = ["3z"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("31.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_32():
    """
    Case #32
    Dealer should open yakuhai with two valued pairs in the hand.
    """

    reproducer_command = "python reproducer.py --log 2020112307gm-0089-0000-c294daec --player 3 --wind 8 --honba 0 --action enemy_discard --tile 2z"
    needed_meld = {"type": "pon", "tiles": "222z"}
    tile_after_meld = "3m"

    result_meld, result_tile_after_meld = _run_reproducer("32.txt", reproducer_command)
    assert result_meld.type == needed_meld["type"]
    assert TilesConverter.to_one_line_string(result_meld.tiles) == needed_meld["tiles"]
    assert TilesConverter.to_one_line_string([result_tile_after_meld.tile_to_discard_136]) == tile_after_meld


def test_system_case_33():
    """
    Case #33
    Bot wrongly detected honitsu for shimocha discards.
    """

    reproducer_command = "python reproducer.py --log 2020112309gm-0089-0000-53e7b431 --player 1 --wind 3 --honba 1 --action draw --n 1 --tile 6m"
    allowed_discards = ["6p"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("33.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_34():
    """
    Case #34
    Bot pushed too much against multiple threats.
    """

    reproducer_command = "python reproducer.py --log 2020112317gm-0089-0000-f4d22bba --player 2 --wind 6 --honba 0 --action draw --n 1 --tile 8s"
    allowed_discards = ["9p"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("34.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_35():
    """
    Case #35
    Must riichi.
    """

    reproducer_command = "python reproducer.py --log 2020112504gm-0089-0000-e125fd6f --player 2 --wind 8 --honba 0 --action draw --n 1 --tile 2s"
    allowed_discards = ["3s"]
    with_riichi = True

    result, with_riichi_result = _run_reproducer("35.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_36():
    """
    Case #36
    Must fold with north tiles.
    """

    reproducer_command = "python reproducer.py --log 2020112504gm-0089-0000-94960883 --player 1 --wind 1 --honba 0 --action draw --n 2 --tile 9p"
    allowed_discards = ["4z"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("36.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_37():
    """
    Case #37
    Must open meld to secure 3rd place.
    """

    reproducer_command = "python reproducer.py --log 2020112504gm-0029-0000-ca8a957c --player 2 --wind 8 --honba 0 --action enemy_discard --n 1 --tile 4z"
    needed_meld = {"type": "pon", "tiles": "444z"}
    tile_after_meld = "1p"

    result_meld, result_tile_after_meld = _run_reproducer("37.txt", reproducer_command)
    assert result_meld.type == needed_meld["type"]
    assert TilesConverter.to_one_line_string(result_meld.tiles) == needed_meld["tiles"]
    assert TilesConverter.to_one_line_string([result_tile_after_meld.tile_to_discard_136]) == tile_after_meld


def test_system_case_38():
    """
    Case #38
    It is fine to riichi with that hand.
    """

    reproducer_command = "python reproducer.py --log 2020112505gm-0089-0000-1a2861c9 --player 3 --wind 5 --honba 0 --action draw --n 1 --tile 9s"
    allowed_discards = ["8p"]
    with_riichi = True

    result, with_riichi_result = _run_reproducer("38.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_39():
    """
    Case #39
    Better to fold that hand.
    """

    reproducer_command = "python reproducer.py --log 2020112507gm-0089-0000-07c68413 --player 0 --wind 4 --honba 0 --action draw --n 2 --tile 4m"
    allowed_discards = ["3m", "2p", "8p"]
    with_riichi = False

    result, with_riichi_result = _run_reproducer("39.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result


def test_system_case_40():
    """
    Case #40
    We should riichi with 2m, not with 5m.
    """

    reproducer_command = "python reproducer.py --log 2020113000gm-0009-7994-1460f04f --player 2 --wind 6 --honba 0 --action draw --n 1 --tile 3m"
    allowed_discards = ["2m"]
    with_riichi = True

    result, with_riichi_result = _run_reproducer("40.txt", reproducer_command)
    assert TilesConverter.to_one_line_string([result]) in allowed_discards
    assert with_riichi == with_riichi_result
