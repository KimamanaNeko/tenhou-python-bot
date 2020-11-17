import os
from pathlib import Path

from system_testing.cases import SYSTEM_TESTING_CASES, ACTION_DISCARD


class DocGen:
    @staticmethod
    def generate_documentation():
        system_testing_folder = Path(__file__).parent.absolute()
        project_folder = Path(__file__).parent.parent.parent.absolute()
        doc_file = system_testing_folder.parent.parent / 'doc' / 'system_testing.md'
        doc_content = []
        for case in SYSTEM_TESTING_CASES:
            index = case['index']
            relative_image_path = (system_testing_folder / 'fixtures' / f"{index}.png").relative_to(project_folder)

            doc_content.append(f'# Case {index}')

            if case['action'] == ACTION_DISCARD:
                doc_content.append(f"`Action: {ACTION_DISCARD}, allowed discard: {', '.join(case['allowed_discards'])}`")
                doc_content.append('\n')

            if case['description']:
                doc_content.append(case['description'])

            doc_content.append('```bash')
            doc_content.append(case['reproducer_command'])
            doc_content.append('```')

            doc_content.append(
                f'![image](./{relative_image_path})'
            )

        doc_file.write_text('\n'.join(doc_content))
