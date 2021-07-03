function solution(rows, columns, queries) {
  var answer = [];
  var matrix = new Array (rows)
  for (let i=0; i<rows; i++) {
    matrix[i] = new Array(columns)
    for (let j=0; j<columns; j++) {
      matrix[i][j] = [(1+j)+i*columns]
    }
  }
  console.log(matrix)
  for (let q of queries) {
    var r1 = q[0]-1
    var c1 = q[1]-1
    var r2 = q[2]-1
    var c2 = q[3]-1
    var min_v = rows*columns
    for (let i=c1; i<c2; i++) {
      var v = matrix[r1][i].shift()
      matrix[r1][i+1].push(v)
      if (v < min_v) {
        min_v = v
      }
    }
    for (let i=r1; i<r2; i++) {
      var v = matrix[i][c2].shift()
      matrix[i+1][c2].push(v)
      if (v < min_v) {
        min_v = v
      }
    }
    for (let i=c2; i>c1; i--) {
      var v = matrix[r2][i].shift()
      matrix[r2][i-1].push(v)
      if (v < min_v) {
        min_v = v
      }
    }
    for (let i=r2; i>r1; i--) {
      var v = matrix[i][c1].shift()
      matrix[i-1][c1].push(v)
      if (v < min_v) {
        min_v = v
      }
    }
    answer.push(min_v)
  }
  return answer;
}