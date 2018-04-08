# get_steem_active_users
Python script for STEEM blockchain

Very simple script, need STEEM PYTHON API installed.
The scrypt is an infinite loop that extract all the last hour active users on the STEEM blockchain, and add them into a file. Every hour keeps adding users that are not on the file already, and that have done some activity recorded in the blockchain.

The script is very simple, and not "elegant" at all, but I wrote it in 20 minutes, so please be patient about this, I'll try to update it, and get it a bit more "elegant" when I'll get some time, for now it does it job with no issue ;)
