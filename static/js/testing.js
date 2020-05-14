$(document).ready(function(){
    // Hide displayed paragraphs
    $("#a1").click(function(){
        $("#33c").hide();
    });
        });


$(document).ready(function(){
    // Hide displayed paragraphs
    $("#show").click(function(){
        $("#d12").hide();
        console.log.message(1222s)
    });

    // Show hidden paragraphs
    $(".show-btn").click(function(){
        $("p").show();
    });
});


<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("#hide").click(function(){
    $("p").hide();
    $("h2").show();
  });
  $("#show").click(function(){
    $("p").show();
     $("h2").hide();

  });
});

$(document).ready(function(){

    $("h2").hide();

  });
</script>
</head>
<body>

<p>If you click on the "Hide" button, I will disappear.</p>
<h2> i will hide and show  on hide button</h2>

<button id="hide">Hide</button>
<button id="show">Show</button>


$(document).ready(function(){
  $("#hide").click(function(){
   $("p").hide();
    $("h2").show();
  });
  $("#show").click(function(){
    $("p").show();
     $("h2").hide();

  });
});
$(document).ready(function(){

    $("h2").hide();

  });
</script>
</head>
<body>

<p>If you click on the "Hide" button, I will disappear.</p>
<h2> i will hide and show  on hide button</h2>

<button id="hide">Hide</button>
<button id="show">Show</button>

</body>
</html>
