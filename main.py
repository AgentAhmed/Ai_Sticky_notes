from mcp.server.fastmcp import FastMCP
import os

# Create an instance of FastMCP
mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")


def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("") # Create the file if it doesn't exist
            
@mcp.tool()
def add_note(message:str)-> str:
    """
        Append a new note to the sticky note file

        Args:
            message (str): The note content to be added.

        Return:
            str: Confirmation message indicating the note was saved

    """
    ensure_file()
    with open(NOTES_FILE,"a") as f:
        f.write(message + "\n")
    return "Note saved!" 

@mcp.tool()
def read_notes() -> str:
    """
        Read all notes from the sticky note file

        Return:
            str: All notes as a single string, or a message if no notes exist
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read().strip()
    return notes if notes else "No notes found."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
        Get the latest note from the sticky note file

        Return:
            str: The latest note, or a message if no notes exist
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.readlines()
    return notes[-1].strip() if notes else "No notes found."

@mcp.prompt("What would you like to do with your sticky notes?")
def note_summary_prompt() -> str:
    """
        Prompt for a summary of sticky notes actions

        Return:
            str: A summary of actions taken on sticky notes
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read().strip()
    if not notes:
        return "No notes found. You can add a note."    
    return f"Summarize the current notes: {notes}. What would you like to do next?"