$(document).ready(function(){
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn')
    var searchform = $('#search-form')
    

    $(deleteBtn).on('click', function(e){
        //Faz com que a tag a nao seja interpretada imediatamente como ancora,
        // evitando que o dado seja excluido
        e.preventDefault(); 
        var delLink = $(this).attr('href');
        var result = confirm('Deseja deletar essa pessoa?');

        if(result){
            window.location.href = delLink;
        }
    })
}
);
$(searchBtn).on('click',function(){
    searchform.submit();
});
