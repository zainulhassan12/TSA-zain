//ques = ;
//csrf_token = "{{ csrf_token }}";
//ans =  ;
var selected;
var json = {};
var SelectedAnswer = [];
var clickcheck = null;
var selvalue;
var valueofselection;
var check = false;
var selctedanswer =[];
var ch;
var ques = {{quest|safe}};
var ans = {{answer|safe}};
var quiz = {{len|safe}};
console.log(ans);

for( var i=0;i<ques.length; i++)
{
			var para = document.createElement("p");
            var btn =document.createElement("button");btn.innerHTML="Finish";btn.type='button';btn.className="btn btn-outline-success";btn.id="b1";
			btn.setAttribute("onclick", "RadioFun()")
			var node = document.createTextNode(ques[i]['question']);
			para.appendChild(node);
            var newline = document.createElement('br');
            var co = document.getElementById("z");
			co.style="margin:10px";
            //var form = document.getElementById("form1");
            co.appendChild(para); var olist = document.createElement('ul');
                          olist.id="Answerlist";
	    for (var n=0;n<ans.length;n++)
	    {
			  if(ans[n]['question_id']==ques[i]['id'])
			 {
						 var line = document.createElement('br');
						 var radio = document.createElement('input');
						 radio.type = "radio";
						 radio.name ="choice"+i;
                          radio.id = "radio";
			              radio.value =ans[n]['answer'];
						  var label = document.createElement('label')
						  label.htmlFor = 'contact';
						  var description = document.createTextNode(""+ans[n]['answer']);
			              label.appendChild(description);
//                          var olist = document.getElementById('list1');

                          var ilist = document.createElement('li');
                          ilist.id="option";
                          ilist.setAttribute("onclick","fun(this)");
                          ilist.setAttribute("style",";");
						  ilist.appendChild(radio);
						  ilist.appendChild(label);
						  olist.append(ilist);

			}
			co.append(olist);
	    }
 }

function fun(a){
selvalue=a.closest('li').lastChild.innerHTML;
console.log(selvalue);

}
co.appendChild(btn);


function RadioFun(){
var j= 0;
for (var i =0;i<ques.length; i++)
{
var c = "choice"+i;
var radios = document.getElementsByName(c);
	   for(var k =0;k<radios.length;k++)
		{
			if(radios[k].checked)
			{
				var s = radios[k].value;
				//console.log(s + "|radio");
			}
		}
	    if (s != null)
	    {
			j=j+1;
			console.log(j);
			s = null;
		}
}

	 if (j<ques.length)
		{
			alert("Please Select Answer For Each Question");
		}
     else
    {
		 for (var i=0;i<ques.length; i++)
			{
				var c = "choice"+i;
				var radios = document.getElementsByName(c);
      
				
				  for(var k =0;k<radios.length;k++)
					{
						if(radios[k].checked)
						{
							 var z = radios[k].value;
							 json = {
							 quiz:quiz,
							 question_id:ques[i]['id'],
                             question:ques[i]['question'],
							 answer:z,}
                             SelectedAnswer.push(json);
						}
					}
	          //SelectedAnswer.push(json);
           
			}

          $("#b1").hide();
          var sub = document.createElement('button');sub.id="b2";sub.innerHTML="Submit";
          co.remove();
          var nn = document.getElementById('xx');
          nn.append(sub);
          
	    function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie !== '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            // Does this cookie string begin with the name we want?
	            if (cookie.substring(0, name.length + 1) === (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
}
      var l ={"key":"hello"};
	  $(function() {
	    var csrftoken = getCookie('csrftoken');
	    function csrfSafeMethod(method) {
	        // these HTTP methods do not require CSRF protection
	        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	    }
	
		$.ajaxSetup({
		   beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});
     
        //  var g = JSON.stringify(SelectedAnswer); console.log(g);

        //var da = JSON.stringify(SelectedAnswer);
        // console.log(da +  " click ")

        $('#b2').click(function(e) {
            e.preventDefault(); // prevent form from reloading page
           $.ajax({
					url:'{% url "UserViews:MarkQuiz" %}',
					method: 'POST',
                    dataType: 'json',
                    traditional: true,
                    contentType: 'application/json; charset=utf-8',
                    data:JSON.stringify(SelectedAnswer),
                    //cache: true,
                    success: function(data){
                    alert("Sent For Gradings");
                    $("#b2").hide();

                    var quiz_settings = data[1];
                    var question = data[0];
                    
                   //console.log(quiz_settings, +"  "+ question)
                   // var b = Object.keys(quiz_settings[0])
					//$("#xx").append("<b style="align-items:center">Result</b><hr>"+ act[0]['question'])
                   for (var i = 0;i<data[0].length;i++)
                   { var j = i;j=j+1
                    var act = question[i]['question']
					$("#xx").append('<b>Question# ' +j+ ':</b>'+act[0]['question']+ '<hr>')
					$("#xx").append();
					$("#xx").append('<div class="alert alert-primary col-md-7" role="alert">' +'<b>Your answer:</b>' + question[i]['UserAnswer']+'</div>')
                    var check =  question[i]['status']
                    if (check == true)
                    {
						$("#xx").append('<div class="alert alert-success col-md-6" role="alert">' +'<b>Status:</b>' + question[i]['status']+'</div>')
					}
                    else
					{
						$("#xx").append('<div class="alert alert-danger col-md-6" role="alert">' +'<b>Status:</b>' + question[i]['status']+'</div>')
					}
					
                    $("#xx").append('<div class="alert alert-primary col-md-5" role="alert">' +'<b>Correct one:</b>' + question[i]['correct_is']+'</div>')
					}
					$("#xx").append("<br>")
                    nn.append()
                    },
                    error: function(data){
                    alert(data.status); // the status code
                    alert(data.responseJSON.error); // the message
                    var b = document.createElement('button');b.id="btn3";b.innerHTML="Grades";b.href="{%url 'UserViews:application'%}"
                    }
           
            });
        });
        });

    }
}


