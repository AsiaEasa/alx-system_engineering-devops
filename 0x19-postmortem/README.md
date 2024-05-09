![IMG_7265](https://github.com/AsiaEasa/alx-system_engineering-devops/assets/138696944/62d30722-6375-4e3b-b673-b74ab57214cf)
- Duration: The outage occurred from 8:00 AM to 12:00 PM (GMT).
- Impact: The electronic library website experienced intermittent downtime, with users unable to access resources or perform searches. Approximately 75% of users were affected by the outage.
- Root Cause: The root cause of the issue was identified as a distributed denial of service (DDoS) attack targeting the library's web servers.

Timeline:
- 8:00 AM (UTC): The issue was detected when monitoring alerts indicated a sudden increase in server response times.
- Detection Method: The issue was detected through monitoring alerts set up to track server performance metrics.
- Actions Taken: Engineers investigated server logs and network traffic patterns to identify the cause of the slowdown. Initial assumptions focused on potential server misconfigurations or software bugs.
- Misleading Paths: Initially, there was suspicion of a server misconfiguration or software bug causing the slowdown, leading to attempts to debug server configurations and application code.
- Escalation: As the investigation progressed and the severity of the issue became apparent, the incident was escalated to senior engineering and security teams for further analysis and resolution.
- Resolution: The incident was resolved by implementing rate limiting on incoming traffic to mitigate the effects of the DDoS attack and deploying additional DDoS mitigation measures, including IP blocking and traffic filtering.

Root Cause and Resolution:
- Root Cause: The root cause of the outage was a distributed denial of service (DDoS) attack targeting the electronic library’s web servers. In a DDoS attack, malicious actors use a network of compromised computers, known as a botnet, to flood the targeted server with a massive volume of illegitimate traffic. This flood of traffic overwhelms the server’s capacity to handle legitimate requests, resulting in degraded performance or complete unavailability of the service. In this case, the DDoS attack specifically targeted the electronic library’s web servers, causing intermittent downtime and hindering users’ ability to access resources and perform searches.
- Resolution: To address the DDoS attack and restore service functionality, several measures were implemented. First, rate-limiting mechanisms were deployed to restrict the amount of incoming traffic allowed to reach the web servers. By limiting the rate of incoming requests, the impact of the DDoS attack was mitigated, allowing the servers to better handle legitimate user traffic. Additionally, additional DDoS mitigation measures were put in place, including IP blocking and traffic filtering. IP blocking involves identifying and blocking the IP addresses associated with the malicious traffic, effectively preventing them from reaching the web servers. Traffic filtering techniques were also employed to identify and filter out illegitimate traffic, further reducing the strain on the servers. These combined measures helped to mitigate the effects of the DDoS attack and restore normal service functionality to the electronic library’s website.

Corrective and Preventative Measures:
- Improvements/Fixes:
  - Implement enhanced DDoS protection mechanisms, such as traffic scrubbing services or cloud-based DDoS mitigation solutions.
  - Regularly review and update security policies to adapt to evolving threats.
- Tasks:
  - Conduct a thorough review of network infrastructure to identify potential vulnerabilities and weaknesses.
  - Implement rate limiting and traffic filtering rules to prevent future DDoS attacks.
  - Train staff on DDoS attack detection and mitigation techniques to improve response times in the event of similar incidents. 
