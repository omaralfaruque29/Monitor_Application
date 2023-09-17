#!/bin/bash

INDX=0
kill_process(){
        PROCESS=$1
        SIGNAL_ID=$2
    if [ -z $2 ]
    then
            SIGNAL_ID=9
    fi

    PROCESS_ID=$(pgrep $PROCESS)
    echo $PROCESS_ID
    if [ -z "$PROCESS_ID" ] ;then
            echo "NO RUNNING $1 PROCESS"
    else
            for PID in $PROCESS_ID
            do
                    echo "Process Id of $PROCESS : $PID"
                    : `kill -$SIGNAL_ID  $PID`
                    KILL_STATUS=$?

                    if [[ $KILL_STATUS != 0 ]]
                    then
                            echo "PROCESS TERMINATION ERROR"
                    fi
            done
    fi

}

kill_process gunicorn

exit 0

