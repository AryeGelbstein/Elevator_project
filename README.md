# Elevator Project

## Overview
This project simulates an elevator system in a building using Python and Pygame. The simulation includes multiple floors and elevators, with realistic movement and user interactions.

## Features
- **Building Simulation**: Configurable number of floors and elevators.
- **Elevator Movement**: Elevators respond to floor requests and move accordingly.
- **User Interaction**: Users can press floor buttons to call an elevator.
- **Graphical Interface**: Uses Pygame for a visual representation of the building and elevator system.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AryeGelbstein/Elevator_project.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Elevator_project
   ```

3. **Install Dependencies**:
   ```bash
   pip install pygame
   ```

## Usage

1. **Run the Simulation**:
   ```bash
   python main.py
   ```

2. **Interacting with the Simulation**:
   - Click on floor buttons to request an elevator.
   - Use the mouse wheel to scroll through floors.

## Project Structure

- `main.py` - Entry point for the simulation.
- `building.py` - Defines the building structure and manages elevators.
- `elevator.py` - Contains the Elevator class, responsible for movement and queue management.
- `floor.py` - Defines the Floor class and handles floor button interactions.
- `constants.py` - Contains global constants such as screen dimensions and elevator speed.
- `resources/` - Stores images and sounds used in the simulation.

## Notes
- Ensure all resource files (images and sounds) are in the correct paths as defined in `constants.py`.
- Modify `constants.py` to adjust settings such as number of floors, elevators, and movement speed.

Enjoy the simulation!
