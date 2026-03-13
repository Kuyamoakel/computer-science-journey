public class SecondLargestNumber {
    public static void main(String[] args) {

        int[] number = {10, 45, 32, 67, 67, 12};
        int largest = number[0];
        int secondLargest = number[0];
        

        for (int i = 1; i < number.length; i++) {

            if (number[i] > largest) {
                secondLargest = largest;
                largest = number[i];
            }
            //avoids Duplication in arrays
            if (number[i] > secondLargest && number[i] != largest) {
                secondLargest = number[i];
            }
        }
        System.out.println("\t===== List of the Arrays ====");
        for (int numbers : number) {
            System.out.print(numbers + "\t");
        }
        System.out.println("\nLargest: " + largest);
        System.out.println("SecondLargest: " + secondLargest);
        
        

        
    }
}
