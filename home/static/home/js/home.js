console.log('hello from home js')

const tweet = document.getElementById('id_tweet')
const form = document.getElementById('tweet_form')
const url = ""

const csrf = document.getElementsByName('csrfmiddlewaretoken')



form.addEventListener('submit', e => {
    e.preventDefault()

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('tweet', tweet.value)

    $.ajax({
        type: 'POST',
        url: url,
        enctype: 'multipart/form-data',
        data: fd,
        success: function (response) {
            console.log(response)
            create_tweet(response.tweet, response.tweet_id)
            tweet.value = ''
            // const sText = `successfully saved ${response.tweet}`

        },
        error: function (error) {
            console.log(error)
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})

function create_tweet(tweet_content, tweet_id) {
    var parent_div = document.createElement('div');

    var card_body = document.createElement('div')
    var profile_link = document.createElement('a')
    var row = document.createElement('div')
    var col_1 = document.createElement('div')
    var user_img = document.createElement('img')
    var user_name = document.createElement('strong')
    var tweet_link = document.createElement('a')
    var twt_text = document.createElement('h4')

    var like_comnt_row = document.createElement('div')

    var cmnt = document.createElement('div')
    var cmnt_link = document.createElement('a')
    var cmt_img = document.createElement('img')

    var like = document.createElement('div')
    var like_link = document.createElement('a')
    var cmnt_count = document.createElement('span')
    var like_count = document.createElement('span')
    var cmnt_text = document.createTextNode("0")
    var like_text = document.createTextNode("0")
    cmnt_count.appendChild(cmnt_text)
    like_count.appendChild(like_text)
    var like_img = document.createElement('img')

    like_count

    parent_div.id = 'container';
    parent_div.className = 'card text-white bg-dark mb-1';
    // parent_div.innerHTML = tweet_content;

    card_body.className = 'card-body'
    // card_body.innerHTML = tweet_content
    // link to profile
    profile_link.href = "profile/" + cur_user
    profile_link.style = 'text-decoration: none; color: white;'

    row.className = 'row'
    col_1.className = 'col-1'
    // user_img
    user_img.src = profile_pic_url
    // user_img.className = 'profile'
    user_img.style = 'width:50px; height:50px; border-radius: 50%; object-fit: cover;'
    // user name
    user_name.className = 'col-1'
    user_name.innerHTML = cur_user




    col_1.appendChild(user_img)

    row.appendChild(col_1)
    row.appendChild(user_name)
    profile_link.appendChild(row)

    //  tweet content
    tweet_link.href = 'tweet_detail/' + tweet_id
    tweet_link.style = 'text-decoration: none; color: white;'

    twt_text.innerHTML = tweet_content


    // Like and comment
    like_comnt_row.className = 'row'
    cmnt.className = 'col-1'

    cmnt_link.href = 'tweet_detail/' + tweet_id
    cmnt_link.style = 'text-decoration: none; color: white;'

    cmt_img.src = '/static/resource/site_icons/comment.svg'
    cmt_img.style = 'width:65%; height:65%'

    like.className = 'col-1'
    like_link.href = 'liked/' + tweet_id

    like_img.src = '/static/resource/site_icons/heart.svg'
    like_img.style = 'width:20px;'

    like_link.appendChild(like_img)
    like.appendChild(like_link)
    like.appendChild(like_count)

    cmnt_link.appendChild(cmt_img)
    cmnt.appendChild(cmnt_link)
    cmnt.appendChild(cmnt_count)

    like_comnt_row.appendChild(cmnt)

    like_comnt_row.appendChild(like)

    card_body.appendChild(profile_link)

    tweet_link.appendChild(twt_text)

    card_body.appendChild(tweet_link)
    card_body.appendChild(like_comnt_row)

    parent_div.appendChild(card_body)
    document.body.childNodes[5].insertBefore(parent_div, document.body.childNodes[5].childNodes[11])
}