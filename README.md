# hacker-scripts

## event_notice

Send email automatically using Python.  

### 1️⃣ Create a shell script

```bash
# Create the shell script
nano /path/to/event_notice.sh
```

Add the following content to event_notice.sh:
```bash
#!/bin/bash
python3 /path/to/event_notice.py
```

Make it executable:
```bash
chmod +x /path/to/event_notice.sh
```

Open your crontab:
```bash
crontab -e
```

Add this line to run the script every Tuesday at 9:00 AM:
```bash
0 9 * * 2 /path/to/event_notice.sh
```

0 9 * * 2 → runs at 09:00 every Tuesday.

Make sure to replace /path/to/ with the full path to your script and shell file.
