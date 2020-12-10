from pathlib import Path

from system_testing.cases import ACTION_CRASH, ACTION_DISCARD, ACTION_MELD, SYSTEM_TESTING_CASES

system_testing_folder = Path(__file__).parent.absolute()
project_folder = Path(__file__).parent.parent.parent.absolute()


class TestsGen:
    @staticmethod
    def generate_documentation():
        tests_file = Path(__file__).parent.absolute() / "test_system.py"
        result = []

        result.append("# WARNING. It is an autogenerated file, don't change it manually.")

        result.append("import pytest")

        # header
        result.append(
            """import logging
from pathlib import Path

from mahjong.tile import TilesConverter
from reproducer import TenhouLogReproducer, parse_reproducer_args

logger = logging.getLogger()
system_testing_folder = Path(__file__).parent.absolute()

"""
        )
        # helper function
        result.append("def _run_reproducer(file_name, reproducer_command):")
        result.append(TestsGen.indent('log_file_path = system_testing_folder / "fixtures" / file_name'))
        result.append(
            TestsGen.indent('opts = parse_reproducer_args(reproducer_command.replace("python ", "").split(" "))')
        )
        result.append(
            TestsGen.indent("reproducer = TenhouLogReproducer(log_id=None, file_path=log_file_path, logger=logger)")
        )
        result.append(
            TestsGen.indent(
                "return reproducer.reproduce(opts.player, opts.wind, opts.honba, "
                "context={'action': opts.action, 'needed_tile': opts.tile, 'tile_number_to_stop': opts.n})"
            )
        )
        result.append("\n")

        for case in SYSTEM_TESTING_CASES:
            index = case["index"]
            action = case["action"]
            description = case["description"]
            reproducer_command = case["reproducer_command"]

            if case.get("skip_reason"):
                result.append(f"@pytest.mark.skip('{case['skip_reason']}')")

            # test header
            result.append(f"def test_system_case_{index}():")
            result.append(TestsGen.indent('"""'))
            result.append(TestsGen.indent(f"Case #{index}"))
            if description:
                result.append(TestsGen.indent(description))
            result.append(TestsGen.indent('"""'))
            result.append(TestsGen.indent(""))

            if action == ACTION_DISCARD:
                allowed_discards = case["allowed_discards"]
                with_riichi = case["with_riichi"]

                # input variables
                result.append(TestsGen.indent(f'reproducer_command = "{reproducer_command}"'))
                result.append(TestsGen.indent(f"allowed_discards = {allowed_discards}"))
                result.append(TestsGen.indent(f"with_riichi = {with_riichi}"))
                result.append(TestsGen.indent(""))

                # assert
                result.append(
                    TestsGen.indent(f'result, with_riichi_result = _run_reproducer("{index}.txt", reproducer_command)')
                )
                result.append(TestsGen.indent("assert TilesConverter.to_one_line_string([result]) in allowed_discards"))
                if with_riichi is not None:
                    result.append(TestsGen.indent("assert with_riichi == with_riichi_result"))
                result.append("\n")

            if action == ACTION_MELD:
                meld = case["meld"]
                tile_after_meld = case["tile_after_meld"]

                # input variables
                result.append(TestsGen.indent(f'reproducer_command = "{reproducer_command}"'))
                result.append(TestsGen.indent(f"needed_meld = {meld}"))
                if tile_after_meld:
                    result.append(TestsGen.indent(f'tile_after_meld = "{tile_after_meld}"'))
                else:
                    result.append(TestsGen.indent("tile_after_meld = None"))
                result.append(TestsGen.indent(""))

                # assert
                result.append(
                    TestsGen.indent(
                        f'result_meld, result_tile_after_meld = _run_reproducer("{index}.txt", reproducer_command)'
                    )
                )

                if meld:
                    result.append(TestsGen.indent('assert result_meld.type == needed_meld["type"]'))
                    result.append(
                        TestsGen.indent(
                            'assert TilesConverter.to_one_line_string(result_meld.tiles) == needed_meld["tiles"]'
                        )
                    )
                    result.append(
                        TestsGen.indent(
                            "assert TilesConverter.to_one_line_string([result_tile_after_meld.tile_to_discard_136]) "
                            "== tile_after_meld"
                        )
                    )
                else:
                    result.append(TestsGen.indent("assert result_meld == needed_meld"))
                    result.append(TestsGen.indent("assert result_tile_after_meld is None"))

                result.append("\n")

            if action == ACTION_CRASH:
                result.append(TestsGen.indent(f'reproducer_command = "{reproducer_command}"'))

                result.append(TestsGen.indent(f'_run_reproducer("{index}.txt", reproducer_command)'))

        tests_file.write_text("\n".join(result))

    @staticmethod
    def indent(string):
        return f"    {string}"
