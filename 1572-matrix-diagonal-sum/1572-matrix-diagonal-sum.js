/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    let count=0;
    for(let i=0;i<mat.length;i++){
        count+=mat[i][i];
    }
    let i=0;
    let j=mat.length-1;
    while(j>=0){
        if(j!==i){
            count+=mat[i][j];
        }
        j--;
        i++;
    }
    return count;
};