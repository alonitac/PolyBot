VALUE=$(echo $3 | sed -e "s/[\/&]/\\&/g")
sed -i "s/{{$2}}/$VALUE/g" $1