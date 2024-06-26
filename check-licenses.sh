#!/bin/sh
# SPDX-License-Identifier: Apache-2.0

APACHE_RAT_VERSION="0.16.1"
APACHE_RAT_JAR="apache-rat-$APACHE_RAT_VERSION.jar"
APACHE_RAT_JAR_URL="https://repo1.maven.org/maven2/org/apache/rat/apache-rat/$APACHE_RAT_VERSION/$APACHE_RAT_JAR"
CACHE_DIRECTORY=".cache"
APACHE_RAT_JAR_PATH="$CACHE_DIRECTORY/$APACHE_RAT_JAR"
APACHE_RAT_EXCLUDE_FILE=".ratignore"

# Set Java command
if [ -n "${JAVA_HOME-}" ]; then
  JAVACMD="$JAVA_HOME/bin/java"
  if [ ! -x "$JAVACMD" ]; then
    die "Java command [$JAVACMD}] not found"
  fi
elif command -v java > /dev/null; then
  JAVACMD=$(command -v java)
else
  die "Environment variable [JAVA_HOME] and command [java] not found"
fi

# Set curl command
if command -v curl > /dev/null; then
  CURLCMD=$(command -v curl)
else
  die "Command [curl] not found"
fi

# Download Apache Rat JAR
if [ ! -d $CACHE_DIRECTORY ]; then
  mkdir $CACHE_DIRECTORY
fi
if [ ! -f $APACHE_RAT_JAR_PATH ]; then
  echo "Downloading Apache Rat from [$APACHE_RAT_JAR_URL]"
  CURL_RESULTS=$(exec $CURLCMD -f --silent --show-error -o "$APACHE_RAT_JAR_PATH" "$APACHE_RAT_JAR_URL")
  if [ $? -ne 0 ]; then
    echo "Failed to download Apache Rat from [$APACHE_RAT_JAR_URL]"
    exit $?
  fi
fi

# Run Apache Rat
REPORT_RESULTS=$(exec $JAVACMD -jar $APACHE_RAT_JAR_PATH --scan-hidden-directories --exclude-file $APACHE_RAT_EXCLUDE_FILE --dir . 2>&1)
if [ $? -ne 0 ]; then
  echo "$REPORT_RESULTS"
  exit $?
fi

UNKNOWN_LICENSES_FOUND=$(echo "$REPORT_RESULTS" | grep --count "??")
echo "Unknown Licenses Found: $UNKNOWN_LICENSES_FOUND"

if [ $UNKNOWN_LICENSES_FOUND -eq 0 ]; then
  RESULT_CODE=0
else
  RESULT_CODE=1
  echo "$REPORT_RESULTS"
fi

exit $RESULT_CODE
