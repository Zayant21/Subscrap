
const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultBox = document.querySelector('.results-card')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value


const sendSearchData = (presub) => {
    $.ajax({
        type: 'POST',
        url:'/search/',
        data:{
            'csrfmiddlewaretoken': csrf,
            'presub':presub, 
        },
        success: (res)=>{
            console.log(res.data)
            const data =res.data
            if (Array.isArray(data)){
                resultBox.innerHTML = "";
                data.forEach(presub=>{
                    resultBox.innerHTML +=`
                    <a href = "/addpresavedsub/${presub.id}" class = "item">
                        <div class = "row mt-xs mb-xs">
                            <div class = "col-3">
                                <img src="${presub.image}" class = "presub-img">
                            </div>
                            <div class = "col-6">
                            <h2>${presub.name}</h2>
                            </div>
                        </div>
                    </a>

                    `
                })
            }
            else {

                if (searchInput.value.length > 0){
                    resultBox.innerHTML =  `<h2>${data}</h2>`
                    
                }
                else{
                    resultBox.classList.add('not-visible')
                }
            }
        },
        error:(err)=>{
            console.log(err)
        }

    })
}

searchInput.addEventListener('keyup', e=> {
    console.log(e.target.value)
    if (resultBox.classList.contains('not-visible')){
        resultBox.classList.remove('not-visible')
    }
    sendSearchData(e.target.value)

})

