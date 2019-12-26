// 當文件已經全載入至記憶體時，開始執行程式
$(document).ready(function() {

    // 清空 product-list
    $('#product-list').empty();
    $('#page').hide()
    $('.foot').hide();
    $('#carouselExampleIndicators').hide();
    $('#it_list').hide();
    $('#navbar').hide();

    login_status = 0
    login_cha = ''
    member_id = ''
    event_id = ''

    var items = null
    var pageCount = 20
    var showItems = (page) => {
        if (items == null) return
        var start = (page - 1) * pageCount
        if (page == last_page) {
            var end = start + last_item - 1
        } else {
            var end = start + pageCount - 1
        }
        $('#product-list').empty();
        for (var i = start; i <= end; i++) {
            newItem(items[i])
        }
    }

    $('.logo').click(function() {
        location.reload();
    })

    var newEvent = (event) => {
        if(event.image=='None'||event.image==''){
            $img = $('<img>').attr('class', 'image').attr('src', "https://cdn.pixabay.com/photo/2016/06/09/00/06/oops-1444975_1280.jpg")
        }else{
            $img = $('<img>').attr('class', 'image').attr('src', event.image)
        }
        //$id = $('<h5>').attr('class', 'name').text('編號 :'+ event.eventID)
        $h3 = $('<h3>').attr('class', 'namee').text(event.eventName)
        $p = $('<p>').attr('class', 'type').text('類型 : ' + event.eventTypeDescription)
        $pri = $('<h3>').attr('class', 'name').text('售價 :'+ event.price)
        $date = $('<h3>').attr('class', 'name').text('日期 :'+ event.eventDate)
        $time = $('<h3>').attr('class', 'name').text('時間 :'+ event.startingTime + " ~ " + event.endingTime)

        $event = $('<div>').attr('class', 'events').append($img).append($h3).append($p).append($pri).append($date).append($time)
        $col = $('<col>').attr('href', '#').append($event)

        $ccol = $col.attr('data-toggle', 'modal').attr('data-target', '#exampleModalCenter').attr('id', event.eventID);

        $('#product-list').append($ccol)

        $ccol.click(function() {
            event_id = event.eventID
            $('.buy').empty()
            $('.buy').append($('<div>').attr('class', 'abcd'))
            //$('.abcd').append($('<id>').text('src', event.id))
            $('.abcd').append($('<p>').text("活動 : " + event.eventName))
            $('.abcd').append($('<p>').text('類型 : ' + event.eventTypeDescription))
            $('.abcd').append($('<p>').text('日期 : ' + event.eventDate))
            $('.abcd').append($('<p>').text('時間 : ' + event.startingTime + " ~ " + event.endingTime))
            $('.abcd').append($('<p>').text('每人限購 : ' + event.salesPerMember + "張"))
            $('.abcd').append($('<div>').addClass('row efgh'))
            $('.efgh').append($('<p>').text("數量 :  "))
            $sel = $('<select>').attr('class', 'selectpicker').attr('id', 'numOfBuy')//.append($('<option>').text("1").attr('value', '1')).append($('<option>').text("2").attr('value', '2')).append($('<option>').text("3").attr('value', '3')).append($('<option>').text("4").attr('value', '4')).append($('<option>').text("5").attr('value', '5'))
            for (var i=1; i<=event.salesPerMember; i++){
                $sel.append($('<option>').text(i).attr('value', i))
            }
            $('.efgh').append($sel)
        })
    }

    var last_item;
    var last_page;
    var newPage = (n) => {
        var pageNum = n / 20
        pageNum = (n % 20 != 0) ? pageNum + 1 : pageNum
        last_item = (n - (Math.floor(pageNum - 1) * 20))
        last_page = (Math.floor(pageNum))
        $('#page-number').empty()

        $la = $('<a>').attr('class', 'page-link').attr('href', '#').attr('tabindex', '-1').attr('aria-disabled', 'true').text('«')
        $lli = $('<li>').attr('class', 'page-item').addClass('disabled').append($la)
        $('#page-number').append($lli)
        $lli.click(function() {
            for (var i = 2; i < pageNum; i++) {
                if ($('.p' + i).hasClass('active')) {
                    $('.p' + (i - 1)).addClass('active')
                    $('.p' + i).removeClass('active')
                    showItems(Number(i) - 1)
                    $rli.removeClass('disabled')
                    if (i == 2) {
                        $lli.addClass('disabled')
                    }
                    break;
                }
            }
        })

        // 插入分頁數字
        for (var i = 1; i <= pageNum; i++) {
            $a = $('<a>').attr('class', 'page-link').attr('href', '#').text(i)



            var strActive = ((i == 1) ? ' active' : '')
            $li = $('<li>').attr('class', 'page-item' + strActive).append($a)
            $llli = $li.addClass('p' + i);
            $('#page-number').append($llli)

            $llli.on('click', function() {
                var i = $(this).text()
                if (i == 1) {
                    $lli.addClass('disabled')
                } else if (i == last_page) {
                    $rli.addClass('disabled')
                } else {
                    $rli.removeClass('disabled')
                    $lli.removeClass('disabled')
                }

                if ($('.page-item').hasClass('active')) {
                    $('.page-item').removeClass('active')
                }
                $('.p' + i).addClass('active');
                showItems(Number(i))

            })
        }

        $ra = $('<a>').attr('class', 'page-link').attr('href', '#').text('»')
        $rli = $('<li>').attr('class', 'page-item').append($ra)
        $('#page-number').append($rli)
        $rli.click(function() {
            for (var i = 1; i < last_page; i++) {
                if ($('.p' + i).hasClass('active')) {
                    $('.p' + (i + 1)).addClass('active')
                    $('.p' + i).removeClass('active')
                    $lli.removeClass('disabled')
                    showItems(Number(i) + 1)
                    if (i == (last_page - 1)) {
                        $rli.addClass('disabled')
                    }
                    break;
                }
            }
        })
    }

    //get all event
    $('#query').on('click', function() {
        $('.first').hide();
        $('.qu').hide();
        $('#carouselExampleIndicators').show().addClass('animated fadeIn');
        $('.foot').show();
        $('#it_list').show();
        $('.container').addClass('animated fadeIn');
        $('#navbar').show();
        $.getJSON('http://0.0.0.0:8008/event/event', function(results, status) {
            //alert(JSON.stringify(results));
            $.each(results, function(index) {
                newEvent(results[index]);
            });

        })
    })
    //get event by ID
    $('#btnSearchEvent').on('click', function() {
        var data = {
            eventID:$('#inputSearchEvent').val()
        }
        $.ajax({url:'http://0.0.0.0:8008/event/eventID', data:data, type:"GET", success:function(results) {
            //alert(results.eventID)
            $('#'+results.eventID).click()
            var t=document.getElementById("inputSearchEvent");
            t.value="";
            }, error: function(aaa){alert("查無編號")
                var t=document.getElementById("inputSearchEvent");
                t.value="";
            }
        })
    })


    $('.btn_add').on('click', function() {
        if(login_cha=='admin'){
            // 取得商品資料
            var data = {
                    eventName: $('#inputEventName').val(),
                    eventType: Number($('#inputEventType').val()),
                    eventDescription: $('#inputEventDescription').val(),
                    eventDate: $('#inputEventDate').val(),
                    startingTime: $('#inputEventStart').val(),
                    endingTime: $('#inputEventEnd').val(),
                    saleRoles: $('#inputEventRoles').val(),
                    salesLimit: Number($('#inputEventTotal').val()),
                    salesPerMember: Number($('#inputEventPer').val()),
                    price: Number($('#inputEventPrice').val()),
                    image: $('#inputEventImage').val()
            }

            // 新增商品
            $.post('http://0.0.0.0:8008/event/addEvent', data, function(response, status) {
                if(response){
                    alert('新增成功')
                    location.reload();
                }else{
                    alert('新增失敗')
                }

            })
        }else{
            alert("僅管理員可執行此動作")
        }

    })

    //刪除活動
    $('.btn_delete').on('click', function() {
        // 取得商品資料
        var data = {
            eventID: $('#deleteEventID').val()
        }

        // 刪除商品
        $.ajax({url: 'http://0.0.0.0:8008/event/deleteEvent', data: data, type: 'DELETE', success: function (response) {
                if(response){
                    alert('刪除成功')
                    location.reload();
                }else{
                    alert('刪除失敗')

                }
            }, error: function(aaa){alert("查無編號")
                var t=document.getElementById("deleteEventID");
                t.value="";
            }})
    })

    //修改活動
    $('.btn_modify').on('click', function() {
        // 取得商品資料
        var data = {
            eventID: $('#inputEventID').val(),
            eventName: $('#modifyEventName').val(),
            eventType: Number($('#modifyEventType').val()),
            eventTypeDescription: $('#modifyEventTypeDescription').val(),
            eventDescription: $('#modifyEventDescription').val(),
            eventDate: $('#modifyEventDate').val(),
            startingTime: $('#modifyEventStart').val(),
            endingTime: $('#modifyEventEnd').val(),
            saleRoles: $('#modifyEventRoles').val(),
            salesLimit: Number($('#modifyEventTotal').val()),
            salesPerMember: Number($('#modifyEventPer').val()),
            price: Number($('#modifyEventPrice').val()),
            image: $('#modifyEventImage').val()
        }

        // 刪除商品
        $.ajax({url: 'http://0.0.0.0:8008/event/modifyEvent', data: data, type: 'POST', success: function (response) {
                if(response){
                    alert('修改成功')
                    location.reload();
                }else{
                    alert('修改失敗')

                }
            }, error: function(aaa){alert("修改失敗，請正確輸入格式")
                var t=document.getElementById("deleteEventID");
                t.value="";
            }})
    })

    //登入
    $('#login').on('click', function() {
        // 取得商品資料

        var data = {
            userAccount: $('#accountInput').val(),
            userPassword: $('#passwordInput').val()
        }

        // 新增商品
        $.ajax({url:'http://0.0.0.0:8008/member/login', data: data, type: "POST", success: function(response, status) {
            if(response){
                alert('登入成功')
                $("#dropdownMenu1").click()
                var t=document.getElementById("accountInput");
                t.value="";
                t=document.getElementById("passwordInput");
                t.value="";
                t=document.getElementById("dropdownMenu1");
                t.innerHTML="登出";
                login_status = 1
                login_cha = data.userAccount
                member_id = response.memberID
            }else{
                alert('登入失敗')
            }

        }, error: function(){
                alert("帳號或密碼錯誤")
                $("#dropdownMenu1").click()
                var t=document.getElementById("accountInput");
                t.value="";
                t=document.getElementById("passwordInput");
                t.value="";
            }
        })
    })

    //購買活動
    $('.btn_buy').on('click', function() {
        if(login_status==1){
        // 取得商品資料
        var data = {
            memberID: member_id,
            eventID: event_id,
            numberOfTicket: Number($('#numOfBuy').val()),
        }

        $.ajax({url: 'http://0.0.0.0:8008/sales/buyTicket', data: data, type: 'POST', success: function (response) {
                if(response){
                    alert('購買成功')
                }else{
                    alert('購買失敗')

                }
            }, error: function(){alert("修改失敗，請正確輸入格式")
            }}
        )
        }else{
            alert("登入會員，即可購票")
        }


    })




    $("#dropdownMenu1").click(function(){
        if(login_status==1){
            if(confirm("確認登出?")){
                login_status=0
                login_cha=''
                member_id = ''
                var t=document.getElementById("dropdownMenu1");
                t.innerHTML="登入";
            }   
        }else{
            $("#drop-menu").slideToggle("slow");
            $(".xs1").toggle();
            $(".xs2").toggle();
        }
    });


})