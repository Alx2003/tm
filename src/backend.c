#include <stdio.h>
#include <time.h>
#include <unistd.h>

int main() {
    clock_t prev_times, curr_times;

    // Get the initial CPU time
    prev_times = clock();

    // Loop to monitor CPU utilization
    while (1) {
        // Get current CPU time
        curr_times = clock();
        
        // Calculate CPU utilization
        double cpu_utilization = (double)(curr_times - prev_times) / CLOCKS_PER_SEC;

        // Output CPU utilization
        printf("%.2f\n", cpu_utilization * 100);
        fflush(stdout); // Flush the output buffer to ensure Python reads it immediately

        // Wait for some time
        sleep(1);

        // Update previous time
        prev_times = curr_times;
    }

    return 0;
}