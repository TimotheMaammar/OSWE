sudo pip3 install jsbeautifier

mkdir pretty

for f in compressed_*.js; do js-beautify $f > pretty/"${f//compressed_}"; done;
