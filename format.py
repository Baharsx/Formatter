from time import sleep
from tqdm import tqdm

def format_proxies_from_file(input_file="input_proxies.txt", output_file="output_proxies.txt"):
    """
    Reads proxies from an input file, formats them as desired, and saves them to an output file.

    :param input_file: The name of the file containing proxies (one proxy per line)
    :param output_file: The name of the file to save formatted proxies
    """
    try:
        # Step 1: Read the input file
        with open(input_file, "r") as infile:
            # Strip whitespace and remove empty lines
            proxies = [line.strip() for line in infile if line.strip()]

        # If the file is empty or contains no valid data
        if not proxies:
            print("The input file is empty or contains no valid proxies.")
            return

        # Step 2: Write formatted proxies to the output file
        with open(output_file, "w") as outfile:
            for proxy in proxies:
                outfile.write(f'"{proxy}",\n')

        print(f"\nAll proxies have been successfully formatted and saved to '{output_file}'.")

        # Step 3: Show a fancy animation
        print("\nSaving completed! Loading a fancy logo for you...\n")
        for _ in tqdm(range(50), desc="Generating Logo", ascii=" █", colour="green"):
            sleep(0.05)  # Simulate processing time

        print("""






██████╗  █████╗ ██╗  ██╗ █████╗ ██████╗ ███████╗██╗  ██╗
██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝
██████╔╝███████║███████║███████║██████╔╝███████╗ ╚███╔╝
██╔══██╗██╔══██║██╔══██║██╔══██║██╔══██╗╚════██║ ██╔██╗
██████╔╝██║  ██║██║  ██║██║  ██║██║  ██║███████║██╔╝ ██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝


        """)
        print("🎉 Done! Enjoy your formatted proxies! 🎉")

    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' was not found. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
if __name__ == "__main__":
    # Specify input and output files
    input_file = "input_proxies.txt"  # Name of the input file
    output_file = "formatted_proxies.txt"  # Name of the output file

    # Execute the proxy formatting function
    format_proxies_from_file(input_file, output_file)
