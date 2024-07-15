def calculate_body_shape(bust, waist, high_hip, hip):
    # Calculate the waist-hip ratio (WHR)
    whr = waist / hip

    # Determine body shape based on measurements
    if bust > hip:
        body_shape = "Apple (Inverted Triangle)"
    elif (hip > bust) and (hip > waist):
        body_shape = "Pear (Spoon, Bell, Triangle)"
    elif (abs(bust - hip) <= 1) and (waist < bust and waist < hip):
        body_shape = "Hourglass (X shape, Triangles opposing, Facing inwards)"
    else:
        body_shape = "Banana (Straight, Rectangle)"

    return body_shape, whr

def main():
    # Get user input for measurements
    bust = float(input("Enter your bust measurement (in inches): "))
    waist = float(input("Enter your waist measurement (in inches): "))
    high_hip = float(input("Enter your high hip measurement (in inches): "))
    hip = float(input("Enter your hip measurement (in inches): "))

    # Calculate body shape and WHR
    body_shape, whr = calculate_body_shape(bust, waist, high_hip, hip)

    # Output results
    print(f"Your body shape is: {body_shape}")
   
if __name__ == "__main__":
    main()
