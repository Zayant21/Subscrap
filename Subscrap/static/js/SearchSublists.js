const searchField  =document.querySelector("#searchsublist");

const tableOutput = document.querySelector(".table-output");
const subscriptiontable = document.querySelector(".subscriptions-table");
tableOutput.style.display = "none";
const tbody = document.querySelector(".table-body")



searchField.addEventListener('keyup', (e) => {
    const searchsublist = e.target.value;


    if (searchsublist.trim().length > 0){
    console.log("searchsublist", searchsublist);
    tbody.innerHTML = "";
    fetch("/search_user_sublist", {
        body: JSON.stringify({SearchText: searchsublist}),
        method: "POST"
    })

        .then((res) => res.json())
        .then((data)=> {
        console.log("data", data);
        subscriptiontable.style.display = "none";
        tableOutput.style.display = "block";
        

        if (data.length === 0){
        }
        
        else{
            
            subscriptiontable.style.display = "none";
                data.forEach(item => {
                    
                    tbody.innerHTML+= `
                    <td>
                    <a href="${item.website}" class="logo-link">
                    <img src="/images/${item.image}" width="35" height="35" style="border-radius: 27%;">
                    </a>
                    </td>
                        <td>${item.name}</td>
                        <td>${item.cost}$</td>
                        <td>${item.startDate}</td>
                        <td>${item.dueDate}</td>
                        <td>${item.subtype}</td>
                        <td>${item.is_active}</td>

                        <td>
                         <a href= "/editsubscription/${item.id}" > <span class = "btn btn-Default">  &#9998; </span></a>                       
                         <a href="/deletelist/${item.id}">  <span class = "btn btn-Default " onclick="return confirm('Are you sure you want to delete this item?');"> &#128465; </a>
                        </td>
                        
                    </tr>`;

                });

        }

    });

    }
    else {
        tableOutput.style.display = "none";
        subscriptiontable.style.display = "block";
    
    }


});