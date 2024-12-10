import argparse
from datasets import load_dataset
import os

def download_and_save_dataset(dataset_name, split, output_file):
    """
    Downloads a Hugging Face dataset and saves it as a CSV file.
    prereqs: huggingface datasets library (pip install datasets)
    """
    try:
        # Load the dataset
        print(f"Loading dataset: {dataset_name} with split: {split}")
        dataset = load_dataset(dataset_name, split=split)

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_file)
        os.makedirs(output_dir, exist_ok=True)

        # Save the dataset as a CSV
        print(f"Saving dataset to: {output_file}")
        dataset.to_csv(output_file, index=False)
        print("Dataset saved successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Download a Hugging Face dataset and save it as a CSV.")
    parser.add_argument(
        "dataset_name",
        type=str,
        help="Name of the dataset to download (e.g., 'sayhan/strix-philosophy-qa')."
    )
    parser.add_argument(
        "--split",
        type=str,
        default="train",
        help="Split of the dataset to download (e.g., 'train', 'test'). Default is 'train'."
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default=r"C:\data\hf_csvs\output.csv",
        help=(
            "Path to save the dataset CSV file (e.g., "
            r"'C:\data\hf_csvsoutput.csv'). "
            "Default is 'C:\\data\\hf_csvs\\output.csv'."
        )
    )

    args = parser.parse_args()

    # Call the function with parsed arguments
    download_and_save_dataset(args.dataset_name, args.split, args.output_file)
