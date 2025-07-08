from src.main import main

if __name__ == "__main__":
    main()

from epitope_select import select_epitope

epitope = select_epitope("inputs/bepipred_output.csv")
if epitope:
    start, end, sequence = epitope
    print(f"Selected epitope: {start}-{end}, {sequence}")
    