$(function() {


    // $(document).ready(function () {
    //     $(document).ajaxStart(function () {
    //         $("#loading").show();
    //     }).ajaxStop(function () {
    //         $("#loading").hide();
    //     });
    // });

    $('#btnLogin').click(function() {
 
        $.ajax({
            url: '/dashboard',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('tbody tr').click(function(event) {
        tr = event.target.closest('tr');
        var domain=$(tr).attr('domain');
        var code=$(tr).attr('id');
        var obf_code=$(tr).attr('obf_code');
        
        $('#modal_iframe_url').text('https://'+domain+'/sub/'+code);
        $('#modal_obf_code').text(obf_code);
        $('#myModal').modal('toggle');
    });

    $('.editItem').click(function(event) {
        tr = event.target.closest('tr');
        event.stopPropagation();

        $.ajax({
            url: '/get_link',
            data: {'id': tr.id},
            type: 'POST',
            success: function(response) {
                data = response['data'];
               if (data != null) {
                $('#cid').val(tr.id);
                $('#url').val(data[3]);
                $('#domain').val(data[0]);
                $('#network').val(data[1]);
                $('#publisher').val(data[2]);
               }
               $('#headerText').text('Edit link info');
                $('#saveBtn').hide();
               $('#editBtn').show();
               $('#editModal').modal('toggle');
            },
            error: function(error) {
                console.log(error);
            }
        });
        
     });

    $('.delItem').click(function(event) {
        tr = event.target.closest('tr');
        event.stopPropagation();

        $.ajax({
            url: '/delete_link',
            data: {'link_code': tr.id},
            type: 'POST',
            success: function(response) {
                data = response['data'];
                console.log(data);
                if (data) {
                    location.reload();
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
        
     });

    $('#newPub').click(function(event) {
                $('#cid').val('');
                $('#url').val('');
                $('#network').val('');
                $('#publisher').val('');
                $('#headerText').text('Create new Link');
        $('#saveBtn').show();
        $('#editBtn').hide();
        $('#editModal').modal('toggle');
    });

    $('#saveBtn').click(function(event) {
        var feed = $('#cid').val();
        urlv = $('#url').val();
        publisher = $('#publisher').val();
        network = $('#network').val();
        domain = $('#domain').val();

        $.ajax({
            url: '/save_link',
            data: {'url': urlv, 'network': network, 'domain': domain, 'publisher': publisher},
            type: 'POST',
            success: function(response) {
                if (response['data']) {
                    location.reload();
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
        
     });

    $('#editBtn').click(function(event) {
        var code = $('#cid').val();
        var url = $('#url').val();
        var network = $('#network').val();
        var publisher = $('#publisher').val();
        var domain = $('#domain').val();

        $.ajax({
            url: '/save_link',
            data: {'code': code, 'url': url, 'network': network, 'domain': domain, 'publisher': publisher},
            type: 'POST',
            success: function(response) {
                if (response['data']) {
                    location.reload();
                }
            },
            error: function(error) {
                console.log(error);
            }
        });

     });
    
});
