#!/bin/sh

BASEDIR=$(dirname "$0")

for example_dir in ${BASEDIR}/*/
do
    pushd ${example_dir}
    zip -r ../`basename ${example_dir}` *
    popd
done