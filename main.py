import subprocess

python_files = {
    1: "camera.py",
    2: "video.py",
}
module_descriptions = {
    1: "detection of road signs using the default camera",
    2: "detection of road signs from a selected video recording",
}

def run_script(selected_option):
    python_file = python_files.get(selected_option)

    if python_file:
        subprocess.run(["python", python_file])
    else:
        print("Invalid option")

if __name__ == "__main__":
    while True:
        print("Program modules:")
        for i, file in python_files.items():
            print(f"{i}: {file} - {module_descriptions[i]}")
        print("q: Quit")
        print()
        input_data = input("Enter the number corresponding to the part of the program (q to exit): ")

        if input_data.lower() == 'q':
            break

        try:
            file_number = int(input_data)
            run_script(file_number)
        except ValueError:
            print("Invalid option. Enter a valid number or 'q' to exit the program.")
