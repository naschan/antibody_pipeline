import pandas as pd

def select_epitope(csv_path, threshold=0.5, min_length=15):
    df = pd.read_csv(csv_path)
    df["AboveThreshold"] = df["EpitopeProbability"] > threshold

    epitopes = []
    start = None
    for i, above in enumerate(df["AboveThreshold"]):
        if above and start is None:
            start = i
        elif not above and start is not None:
            if i - start >= min_length:
                region = df.iloc[start:i]
                sequence = "".join(region["AminoAcid"].tolist())
                epitopes.append((start + 1, i, sequence))
            start = None
    if start is not None and len(df) - start >= min_length:
        region = df.iloc[start:]
        sequence = "".join(region["AminoAcid"].tolist())
        epitopes.append((start + 1, len(df), sequence))

    if epitopes:
        print("Found epitope:")
        for e in epitopes:
            print(f"{e[0]}–{e[1]}: {e[2]}")
        return epitopes[0]  # pick the first region
    else:
        print("No epitope above threshold")
        return None
