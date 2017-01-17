def parse_name_and_date(req):
    list_form = []
    temp_list = req.split('&')
    for piece in temp_list:
        p_list = piece.split('=')
        list_form.append(p_list[1])
    return list_form