# Get current date and time
datetime=$(date +"%Y%m%d%H%M%S")

# Get the size of the log files before compression
syslog_size=$(du -h /var/log/syslog | awk '{print $1}')
wtmp_size=$(du -h /var/log/wtmp | awk '{print $1}')

# Create backup directory if it doesn't exist
if [ ! -d "/var/log/backups" ]
then
  mkdir -p /var/log/backups
fi

# Compress syslog and wtmp to backup directory
gzip /var/log/syslog -c > /var/log/backups/syslog-$datetime.gz
gzip /var/log/wtmp -c > /var/log/backups/wtmp-$datetime.gz

# Clear syslog and wtmp
echo "" > /var/log/syslog
echo "" > /var/log/wtmp

# Get the size of the compressed files
syslog_zip_size=$(du -h /var/log/backups/syslog-$datetime.gz | awk '{print $1}')
wtmp_zip_size=$(du -h /var/log/backups/wtmp-$datetime.gz | awk '{print $1}')

# Print the sizes of the log files and compressed files, and compare the sizes
echo "syslog size before compression: $syslog_size"
echo "syslog size after compression: $syslog_zip_size"
echo "wtmp size before compression: $wtmp_size"
echo "wtmp size after compression: $wtmp_zip_size"