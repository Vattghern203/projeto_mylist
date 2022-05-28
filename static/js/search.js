function search_table(tabela, field_input){
  var input, filter, table, tr, td, i;
  input = document.getElementById(field_input);
  filter = input.value.toUpperCase();
  table = document.getElementById(tabela);
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td") ;
    for(j = 0; j < td.length; j++)
    {
      let tdata = td[j];
      if (tdata) {
        if (tdata.innerHTML.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
          break ;
        } else {
          tr[i].style.display = "none";
          }
      }
    }
  }
}