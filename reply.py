# app/repl.py
from app.calculator import Calculator
from app.history_manager import HistoryManager
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def repl():
    """Read-Eval-Print Loop for the calculator."""
    calc = Calculator()
    history_manager = HistoryManager()

    while True:
        try:
            command = input("> ").strip().lower()
            if command == "exit":
                break
            elif command == "menu":
                print("Available commands: add, subtract, multiply, divide, history, clear, exit")
            elif command == "history":
                print(history_manager.get_history())
            elif command == "clear":
                history_manager.clear_history()
                print("History cleared.")
            else:
                # Parse and execute arithmetic commands
                parts = command.split()
                if len(parts) != 3:
                    print("Invalid command. Usage: <operation> <num1> <num2>")
                    continue
                op, a, b = parts
                a, b = float(a), float(b)
                if op == "add":
                    result = calc.add(a, b)
                elif op == "subtract":
                    result = calc.subtract(a, b)
                elif op == "multiply":
                    result = calc.multiply(a, b)
                elif op == "divide":
                    result = calc.divide(a, b)
                else:
                    print("Invalid operation. Use add, subtract, multiply, or divide.")
                    continue
                print(f"Result: {result}")
                history_manager.add_record(f"{a} {op} {b}", result)
        except Exception as e:
            logger.error(f"Error: {e}")
