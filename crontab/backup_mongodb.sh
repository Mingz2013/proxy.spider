#!/bin/sh

DUMP=/usr/bin/mongodump
OUT_DIR=/home/mongod_bak/mongod_bak_now
TAR_DIR=/home/mongod_bak/mongod_bak_list
DATE=`date +%Y_%m_%d`
DB_USER=username
DB_PASS=123456
DAYS=7
TAR_BAK="spider_mongod_bak_$DATE.tar.gz"
cd $OUT_DIR
rm -rf $OUT_DIR/*
mkdir -p $OUT_DIR/$DATE
$DUMP -o $OUT_DIR/$DATE
tar -zcvf $TAR_DIR/$TAR_BAK $OUT_DIR/$DATE
find $TAR_DIR/ -mtime +$DAYS -delete

ftp -n <<-EOF
open 10.141.6.44
user vftpuser vftpuser123456
binary
prompt
lcd $TAR_DIR
put $TAR_BAK
close
bye
EOF
