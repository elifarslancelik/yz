import subprocess
import requests
import os
from dotenv import load_dotenv

load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")


def get_yz(prompt):
    headers = {
        "Authorization": f"Bearer {deepseek_api_key}",
        "Content-Type": "application/json"
    }
    
    system_prompt = """ONLY generate Mac terminal commands. Do not write any explanation, comment, or extra information.
Examples:
-ls
-cd ~/Desktop
-mkdir new_folder
Return only the requested command, do not write ANYTHING else."""

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,  # For more deterministic output
        "max_tokens": 100
    }
    
    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers=headers,
        json=data
    )
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"


def run_code(code):
    try:
        print("\nRunning the code...")

        # Run the code provided by the AI as a terminal command
        result = subprocess.run(code, shell=True, capture_output=True, text=True)
        
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("Error:", result.stderr)

    except Exception as e:
        print(f"Execution Error: {str(e)}")


def main():
    print("Interaction with AI is starting...")
    try:
        while True:
            user_input = input("Give a command to the AI: ")
            
            if user_input.lower() == 'exit':
                print("Exiting...")
                break
            
            code = get_yz(user_input)
            print("\nCode written by AI:\n", code)
            
            # Ask for user confirmation
            choice = input("\nShould the code be executed? (yes/no): ").strip().lower()
            
            if choice == 'yes':
                run_code(code)
            elif choice == 'no':
                print("The code was not executed.")
            else:
                print("Invalid option. The code will not be executed.")
    except KeyboardInterrupt:
        print("\nStopped by user. Goodbye!")

if __name__ == "__main__":
    main()
