var selected;
var clickcheck = null;
var selvalue;
var valueofselection;
var check = false;
var selctedanswer =[];
var ch;
var ques ;
var ans ;
console.log(ques);
console.log(ans);

for( var i=0;i<ques.length; i++)
{
			var para = document.createElement("p");
            var btn =document.createElement("button");btn.innerHTML="Submit";btn.type='button';btn.className="btn btn-outline-success";btn.id="b1";
			var node = document.createTextNode(ques[i]['question']);
			para.appendChild(node);
            var newline = document.createElement('br');
            var co = document.getElementById("z");
            //var form = document.getElementById("form1");
            co.appendChild(para);
	    for (var n=0;n<ans.length;n++)
	    {
			  if(ans[n]['question_id']==ques[i]['id'])
			 {
						 var line = document.createElement('br');
						 var radio = document.createElement('input');
						 radio.type = "radio";
						 radio.name ="choice";
                          radio.id = "radio";
			              radio.value =ans[n]['answer'];
						  var label = document.createElement('label')
						  label.htmlFor = 'contact';
						  var description = document.createTextNode(ans[n]['answer']);
			              label.appendChild(description);
//                          var olist = document.getElementById('list1');
                          var olist = document.createElement('ul');
                          olist.id="Answerlist";
                          var ilist = document.createElement('li');
                          ilist.id="option";
                          ilist.setAttribute("onclick","fun(this)");
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
$("#b1").click(function()
{
});
co.appendChild(btn);

