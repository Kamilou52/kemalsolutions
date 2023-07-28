          $(document).ready(function(){
            $('input[name="modele"]').click(function(){ 
                $('input[name="modele"]').not(this).prop('checked', false);
            });
        });