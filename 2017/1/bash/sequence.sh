#!/bin/bash

sequence() {
  data=$1
  offset=$2
  length=${#data}
  total=0

  for (( i=0; i<length; i++))
  do
    next=$(((i+offset)%length))
    if [ "${data:i:1}" == "${data:next:1}" ]
    then
      total=$((total+${data:i:1}))
    fi
  done

  echo "Sum: ${total}"
}

data=$(<"$(dirname $0)/../input")
sequence ${data} 1
sequence ${data} $((${#data}/2))
