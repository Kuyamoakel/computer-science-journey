import java.util.Scanner;

public class Almozara_SIMCard {
    public static void main(String[] args) {

        // Scanner object used to read user input from the keyboard.
        Scanner in = new Scanner(System.in);

        // Controls whether the program continues running or stops
        boolean isRunning = true;

        // MAIN MENU LOOP
        // Main loop that keeps the menu running while the program is active.
        while (isRunning) {
            System.out.println("\n=== SIMPLE SIM CARD LOADING SYSTEM ===");
            System.out.print("[1] - Buy Regular Load\n[2] - Exit\nEnter your choice: ");
            String userMenu = in.nextLine();

             // I use .equals() to compare Strings instead of using ==
            if (userMenu.equals("1")) {
                // Variable to store the phone number entered by the user
                // It will receive its value inside the validation loop
                String phoneNumber;

                // PHONE NUMBER VALIDATION LOOP
                // This loop will repeat until the user enters a valid phone number
                while (true) {
                    System.out.print("\nPlease enter your phone number: ");
                    phoneNumber = in.nextLine();

                    /*
                     Phone number validation rules:
                     1. The phone number must contain exactly 11 digits.
                     2. It must start with "09".

                     .length() checks the number of characters in the String.
                     .charAt() checks the specific character at a given position.

                     If validation fails, "continue" repeats the loop.
                    */

                    // [JUST EXTRACT] I added this because i've noticed the user can put letters on it, this prevents it.
                    //d+ means only numbers are allowed.
                    if (!phoneNumber.matches("\\d+")) {
                        System.out.println("ERROR: Phone number must contain digits only.");
                        continue;
                    } 

                    if (phoneNumber.length() != 11) {
                        System.out.println("ERROR: Phone number must be exactly 11 digits.");
                        continue;
                    }

                    if (phoneNumber.charAt(0) != '0' || phoneNumber.charAt(1) != '9') {
                        System.out.println("ERROR: Phone number must start with '09'.");
                        continue;
                    }

                    // if both validation pass, break the loop.
                    break;
                }
                /*
                 SIM NETWORK DETECTION

                 substring(1,4) extracts the prefix from the phone number.
                 Example:
                 09171234567
                    ↑↑↑
                    917

                 Integer.parseInt() converts the extracted String into an integer
                 so that comparison operators can be used to detect the network.
                */
                String extractString = phoneNumber.substring(1, 4);
                int numberPrefix = Integer.parseInt(extractString);

                // Variable to store the detected SIM network
                String network;

                /*
                 Determine the SIM network based on the prefix range:

                 901 – 950  →  GLOBE / TM
                 951 – 999  →  SMART / SUN
                */
                if (numberPrefix >= 901 && numberPrefix <= 950) {
                    network = "GLOBE/TM";
                } else if (numberPrefix >= 951 && numberPrefix <= 999) {
                    network = "SMART/SUN";
                } else {
                    // If prefix does not match any range, SIM is unknown
                    System.out.println("ERROR: Unknown SIM Card.");
                    continue;
                }

                // Display the detected network to the user
                
                // LOAD AND PAYMENT VALIDATION LOOP
                // Repeats until the user completes a successful transaction
                while (true) {
                    System.out.println("\nAvailable Product for " + network);
                    System.out.print("Enter Load Amount: ");
                    double loadAmount = in.nextDouble();
                    in.nextLine(); // clears the input buffer

                    // Valid load amount must be between 15 and 150.
                    if (loadAmount >= 15 && loadAmount <= 150) {
                        System.out.print("Enter your Cash Payment: ");
                        double userPayment = in.nextDouble();
                        in.nextLine(); // clears the input buffer
                        
                         /*
                         Check if the user's payment is sufficient.
                         If payment is less than the load amount,
                         an error message is displayed.
                        */
                        if (userPayment < loadAmount) {
                            System.out.println("ERROR: Your payment should not be less than your load amount!");
                        } else {
                            // Successful transaction
                            // Calculate and display the change
                            System.out.println("Payment Successful. Your change due is " + (userPayment - loadAmount));
                            break;
                        }
                    } else {
                        System.out.println("ERROR: Please enter a load amount from '15-150'.");
                    }
                }

            // For exiting the program
            } else if (userMenu.equals("2")) {
                System.out.println("THANK YOU! Good Bye...");
                isRunning = false;
            } else {
                // Error message for invalid menu choice
                System.out.println("Invalid Input!");
            }
        }
        // Close the scanner to free system resources
        in.close();
    }
}