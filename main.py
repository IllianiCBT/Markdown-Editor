def editor():
    options = {"plain": '',
               "bold": '**',
               "italic": '*',
               "header": '',
               "link": '',
               "inline-code": '`',
               "ordered-list": '',
               "unordered-list": '',
               "new-line": ''}

    text_processed = ''

    while True:
        formatter = input("Choose a formatter: ")

        if formatter == "!done":
            with open('output.md', 'w') as file:
                file.write(text_processed)

            exit()

        elif formatter == "!help":
            # seperator dictated by JetBrains task
            print(f"Available formatters: {' '.join(str(x) for x in options.keys())}")
            print("Special commands: !help !done")

        elif formatter not in options.keys():
            print("Unknown formatting type or command")

        elif formatter in options:
            if formatter == 'new-line':
                text_processed = f"{text_processed}\n"

                print(text_processed)

            elif formatter == 'link':
                text_processed = f"{text_processed}[{input('Label: ')}]({input('URL: ')})"

                print(text_processed)

            elif formatter == 'header':
                while True:
                    level = int(input("Level: "))

                    if level not in range(1, 6):
                        print("The level should be within the range of 1 to 6")
                        continue
                    else:
                        break

                if text_processed == '':  # check whether this is the first line of the document
                    text_processed = f"{'#' * level} {input('Text: ')}\n"
                else:
                    text_processed = f"{text_processed}\n{'#' * level} {input('Text: ')}\n"

                print(text_processed)

            elif formatter == 'ordered-list' or formatter == 'unordered-list':
                while True:
                    row_count = int(input("Number of rows: "))

                    if row_count < 1:
                        print("The number of rows should be greater than zero")
                        continue
                    else:
                        break

                for row in range(1, row_count + 1):
                    if text_processed == '':
                        if formatter == 'ordered-list':
                            text_processed = f"{row}. {input('Text: ')}"
                        else:
                            text_processed = f"* {input('Text: ')}"
                    else:
                        if formatter == 'ordered-list':
                            text_processed = f"{text_processed}\n{row}. {input('Text: ')}"
                        else:
                            text_processed = f"{text_processed}\n* {input('Text: ')}"

                    if row == row_count:
                        text_processed = f"{text_processed}\n"

                    print(text_processed)

            else:
                text_processed = f"{text_processed}{options[formatter]}{input('Text: ')}{options[formatter]}"

                print(text_processed)


if __name__ == '__main__':
    editor()
