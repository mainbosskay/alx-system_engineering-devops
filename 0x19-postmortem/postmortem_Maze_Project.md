# Maze Project Outage
June 1, 2024

* Following the service disruption of the Maze Project on June 1, 2024, this incident report aims to provide a comprehensive overview of the events that led to the interruption of our platform's functionality. We recognize the significant impact this incident had on our users and sincerely apologize for any inconvenience experienced during this period.

## Issue Summary
Duration of Outage: June 1, 2024, 15:00pm - June 1, 2024, 17:30pm
- Impact: The Maze Project game became unresponsive and crashed for all users attempting to start a new game. Approximately 100% of users were affected during this period, experiencing immediate crashes upon launching the game.
- Root Cause: An unhandled exception caused by a memory leak in the raycasting logic, specifically when rendering walls, led to excessive memory consumption and crashes.

## Timeline
- **15:00 pm: Issue detected via a spike in crash reports from the game’s automatic crash reporting system.
- **15:05 pm: Initial investigation began by the on-call engineer who noticed the correlation between crashes and the wall rendering function.
- **15:15 pm: Assumption made that the issue was due to recent changes in the texture loading module.
- **15:30 pm: Debugging efforts focused on texture handling, but no issues were found.
- **15:45 pm: Further investigation revealed that memory usage was abnormally high during raycasting operations.
- **16:00 pm: Issue escalated to the graphics rendering team.
- **16:15 pm: The team identified that the memory leak was caused by improper management of dynamically allocated memory in the raycasting loop.
- **16:45 pm: The memory leak was fixed, and a patch was prepared.
- **17:00 pm: Patch deployed to production.
- **17:30 pm: System stabilized, and no further crashes reported.

## Root Cause and Resolution
## Root Cause:
- The issue was traced to the raycasting logic where dynamically allocated memory for rendering walls was not properly freed. Each frame rendered accumulated memory usage, leading to a rapid increase in memory consumption and eventual crashes.

- Specifically, the raycasting loop was allocating new memory for each wall slice rendered but did not include proper deallocation, resulting in a memory leak. This oversight caused the game to run out of available memory, leading to crashes when users attempted to start a new game.

## Resolution:
- The resolution involved identifying all points in the raycasting logic where memory was being allocated and ensuring that corresponding deallocation was properly implemented. The primary changes included:
- Implementing proper memory management routines to free allocated memory after each frame.
- Adding additional checks to ensure that no dangling pointers were left after memory was freed.
- The patch was tested in a staging environment to confirm that the memory leak was resolved before deploying it to production.

## Corrective and Preventative Measures

## Improvements:
+ To prevent similar issues in the future, several improvements were identified:
+ Enhance code reviews specifically focusing on memory management practices.
+ Implement automated tools to detect memory leaks and other memory-related issues during development.
+ Improve logging and monitoring to detect abnormal memory usage patterns early.

## Tasks:

Patch Memory Management:
+ Review and refactor the raycasting logic to ensure proper memory allocation and deallocation.
+ Implement additional unit tests for memory management.

Enhance Code Reviews:
+ Train developers on best practices for memory management in C.
+ Include a checklist for memory management in the code review process.

Automated Memory Leak Detection:
+ Integrate tools like Valgrind into the CI/CD pipeline to automatically detect memory leaks.
+ Schedule regular scans of the codebase for memory-related issues.

Improve Monitoring:
+ Add detailed monitoring of memory usage in the production environment.
+ Set up alerts for abnormal memory consumption to catch issues before they escalate.

User Communication:
+ Notify affected users of the issue and the steps taken to resolve it.
+ Provide updates on any further improvements to enhance user confidence.
By implementing these measures, we aim to improve the robustness of the Maze Project and enhance the overall user experience by ensuring that similar issues do not recur in the future.
