def fuzzy_comfort_system():
    print("Welcome to the Room Comfort Fuzzy Logic System!")
    
    # Input temperature and humidity
    temperature = float(input("Enter the room temperature (°C): "))
    humidity = float(input("Enter the room humidity (%): "))
    
    # Fuzzy logic rules
    if temperature < 18 or humidity > 70:
        comfort_level = "Uncomfortable (Too Cold or Humid)"
    elif 18 <= temperature <= 24 and 40 <= humidity <= 60:
        comfort_level = "Comfortable"
    elif temperature > 24 or humidity < 40:
        comfort_level = "Uncomfortable (Too Hot or Dry)"
    else:
        comfort_level = "Moderately Comfortable"
    
    print(f"\nComfort Level: {comfort_level}")

# Run the fuzzy logic system
fuzzy_comfort_system()
