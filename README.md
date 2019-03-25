Stuff for the pi vision in 2019.

https://robotpy.readthedocs.io/en/stable/install/pynetworktables.html#install-pynetworktables




sync process
the following command and some input files, we can setup and rsync to/from the PI


cat file_list
/home/pi
/etc/rc.local




```

# --exclude=PATTERN exclude files matching PATTERN
# --exclude-from=FILE read exclude patterns from FILE
# --include=PATTERN don’t exclude files matching PATTERN
# --include-from=FILE read include patterns from FILE
# --files-from=FILE read list of source-file names from FILE


#rsync --dry-run

# EXAMPLE:
# SYNC_EXTRA="--dry-run" ./sync_rtp

rsync $SYNC_EXTRA -vazr --delete --files-from=/root/rsync/file_list --exclude-from=/root/rsync/exclude_list 10.25.30.55:/ /
```

