    # project = MC AND status = "In Progress" ORDER BY created DESC
    # project = MC AND status = Resolved ORDER BY created DESC
    # project = MC AND status = Open AND affectedVersion = 1.18.2 ORDER BY votes DESC, created DESC
    # project = MC AND status = Open AND affectedVersion = 1.18.2 AND text ~ "mob" ORDER BY votes DESC, created DESC
    # ?jql=project %20%3D%20 MC %20 AND %20 status %20%3D%20 Open %20 AND %20 affectedVersion %20%3D%20 1.18.2 %20 AND %20 text %20 ~ %20%22 mob %22%20 ORDER %20 BY %20 votes %20 DESC %2C%20 created %20 DESC
    # project = MC AND status = Reopened AND affectedVersion = 1.18.2 AND text ~ "mob" ORDER BY votes DESC, created DESC
    

%20 "空格"

%3D "="

%22 "双引号"

```
project in 
(BDS, MCPE, MCCE, MCD, MCL, REALMS, MC, WEB) 
AND status in 
(Open, "In Progress", Reopened, Resolved, Closed, Postponed) 
AND affectedVersion in 
(EMPTY, 1.13.1.0, 1.14.1.0, "1.18 (Bedrock)", "1.18 (Java)", 1.18.2, 1.18.30, "1.19.0.26 Beta", "1.19.0.27 Preview", "1.6.93 (legacy)", "2.2.12145 (Windows)", "2.2.12146 (New Windows App)", "2.2.12147 (Mac)", "2.2.12148 (Linux)", "2.2.2040 (macOS - 10.9 only)", "2.3.136 (Linux)", "2.3.136 (Mac)", "2.3.136 (New Windows App)", "2.3.136 (Windows)", "PS4 1.85", "PS4 1.88", "PS4 1.89", "PS4 1.90", "PS4 1.91", "PS4 1.92", "PS4 1.93", "PS4 1.94", "PS4 1.95"") 
AND text ~ 
"mob" 
ORDER BY votes DESC, created DESC
```

