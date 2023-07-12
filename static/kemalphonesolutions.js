// $("input:modele").on('click', function() {
//             var $box = $(this);
//             if ($box.is(":checked")) {
//               var group = "input:modele[name='" + $box.attr("name") + "']";
//               $(group).prop("checked", false);
//               $box.prop("checked", true);
//             } else {
//               $box.prop("checked", false);
//             }
//           });

          $(document).ready(function(){
            $('input[name="modele"]').click(function(){ 
                $('input[name="modele"]').not(this).prop('checked', false);
            });
        });