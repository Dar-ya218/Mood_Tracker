import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class MoodTracker:
    def __init__(self):
        self.moods = []
        
    def add_mood(self, rating):
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        mood_emoji = {
            1: "😫",
            2: "😕",
            3: "😊",
            4: "😃",
            5: "🤩"
        }
        self.moods.append({
            'date': date,
            'rating': rating,
            'emoji': mood_emoji.get(rating, "🤔")
        })
        
    def view_moods(self):
        if not self.moods:
            return "No has registrado ningún estado de ánimo todavía!"
            
        history = "\n📊 Tu Historia de Estados de Ánimo:\n"
        for mood in self.moods:
            history += f"{mood['date']}: {mood['emoji']} ({mood['rating']}/5)\n"
        return history

def main():
    tracker = MoodTracker()
    
    while True:
        clear_screen()
        print("😊 Seguimiento de Estado de Ánimo 😊")
        print("\n1. 📝 Registrar estado de ánimo")
        print("2. 📊 Ver historial")
        print("3. 🚪 Salir")
        
        choice = input("\nElige una opción (1-3): ")
        
        if choice == "1":
            print("\n¿Cómo te sientes? (1-5):")
            print("1: Muy mal 😫")
            print("2: Mal 😕")
            print("3: Normal 😊")
            print("4: Bien 😃")
            print("5: Muy bien 🤩")
            
            try:
                rating = int(input("\nTu estado de ánimo: "))
                if 1 <= rating <= 5:
                    tracker.add_mood(rating)
                    print("\n¡Estado de ánimo registrado!")
                else:
                    print("\n¡Por favor ingresa un número entre 1 y 5!")
            except ValueError:
                print("\n¡Por favor ingresa un número válido!")
                
        elif choice == "2":
            print(tracker.view_moods())
            
        elif choice == "3":
            print("\n¡Hasta luego! 👋")
            break
            
        else:
            print("\n¡Opción no válida! Por favor elige 1, 2 o 3.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()