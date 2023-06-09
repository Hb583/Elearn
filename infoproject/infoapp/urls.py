from . import views
from django.urls import path
import infoapp.views


urlpatterns = [
    path('', infoapp.views.home, name='home'),
    path('home', infoapp.views.home, name='home'),
    path('register', infoapp.views.register_st, name='register'),
    path('regtt', infoapp.views.register_tr, name='regtt'),
    path('regadmin', infoapp.views.reg_admin, name='regadmin'),
    path('login', infoapp.views.login, name='login'),
    path('logout', infoapp.views.logout, name='logout'),
    path('contact', infoapp.views.contact, name='contact'),
    path('about', infoapp.views.about, name='about'),
    path('student_home', infoapp.views.student_home, name='student_home'),
    path('teacher_home', infoapp.views.teacher_home, name='teacher_home'),
    path('admin_home', infoapp.views.admin_home, name='admin_home'),
    path('news', infoapp.views.news, name='news'),
    path('add_blog', infoapp.views.add_blog, name='add_blog'),
    path('blogs_admin', infoapp.views.blogs_admin, name='blogs_admin'),
    path('blog_approves/<id>', infoapp.views.blog_approves, name='blog_approves'),
    path('blog_rejects/<id>', infoapp.views.blog_rejects, name='blog_rejects'),
    path('blog_delete/<id>', infoapp.views.blog_delete, name='blog_delete'),
    path('view_blog', infoapp.views.view_blog, name='view_blog'),
    path('update_pr_tr', infoapp.views.update_pr_tr, name='update_pr_tr'),
    path('update_pr_st', infoapp.views.update_pr_st, name='update_pr_st'),
    path('del_admin', infoapp.views.del_admin, name='del_admin'),
    path('edit_admin', infoapp.views.edit_admin, name='edit_admin'),
    path('adm_prof', infoapp.views.adm_prof, name='adm_prof'),
    path('bnb', infoapp.views.bnb, name='bnb'),
    path('subject_tr', infoapp.views.subject_tr, name='subject_tr'),
    path('edit_subject/<id>/<idd>/<idm>', infoapp.views.edit_subject, name='edit_subject'),
    path('add_subject', infoapp.views.add_subject, name='add_subject'),
    path('delete_subject/<id>/<idd>', infoapp.views.delete_subject, name='delete_subject'),
    path('chapter_tr', infoapp.views.chapter_tr, name='chapter_tr'),
    path('edit_chapter/<id>/<idd>/<idk>/<idm>', infoapp.views.edit_chapter, name='edit_chapter'),
    path('delete_chapter/<id>/<idd>/<idk>/<idm>', infoapp.views.delete_chapter, name='delete_chapter'),
    path('add_chapter', infoapp.views.add_chapter, name='add_chapter'),
    path('add_chapter1', infoapp.views.add_chapter1, name='add_chapter1'),
    path('ch_co_tr', infoapp.views.ch_co_tr, name='ch_co_tr'),
    path('edit_content/<id>', infoapp.views.edit_content, name='edit_content'),
    path('delete_content/<id>', infoapp.views.delete_content, name='delete_content'),
    path('add_ch_con', infoapp.views.add_ch_con, name='add_ch_con'),
    path('add_chapter_c0', infoapp.views.add_chapter_c0, name='add_chapter_c0'),
    path('add_chapter_c1', infoapp.views.add_chapter_c1, name='add_chapter_c1'),
    path('stu_sub_selnew', infoapp.views.stu_sub_selnew, name='stu_sub_selnew'),
    path('st_sub_selnew2', infoapp.views.st_sub_selnew2, name='st_sub_selnew2'),
    path('disp_teach', infoapp.views.disp_teach, name='disp_teach'),
    path('stu_buk_teacherr/<id>', infoapp.views.stu_buk_teacherr, name='stu_buk_teacherr'),
    path('stu_buk_teacher', infoapp.views.stu_buk_teacher, name='stu_buk_teacher'),
    path('stu_buk_acc', infoapp.views.stu_buk_acc, name='stu_buk_acc'),
    path('stu_accept/<id>', infoapp.views.stu_accept, name='stu_accept'),
    path('stu_reject/<id>', infoapp.views.stu_reject, name='stu_reject'),
    path('stu_delete/<id>', infoapp.views.stu_delete, name='stu_delete'),
    path('st_book_courses', infoapp.views.st_book_courses, name='st_book_courses'),
    path('acc_chapter/<id>/<ikm>/<sub>', infoapp.views.acc_chapter, name='acc_chapter'),
    path('acc_chapter1', infoapp.views.acc_chapter1, name='acc_chapter1'),
    path('compp', infoapp.views.compp, name='compp'),
    path('st_pr', infoapp.views.st_pr, name='st_pr'),
    path('sched_test', infoapp.views.sched_test, name='sched_test'),
    path('sched_test1', infoapp.views.sched_test1, name='sched_test1'),
    path('sched_test3', infoapp.views.sched_test3, name='sched_test3'),
    path('ex_not', infoapp.views.ex_not, name='ex_not'),
    path('start_test', infoapp.views.start_test, name='start_test'),
    path('save_exam', infoapp.views.save_exam, name='save_exam'),
    path('exam_result1', infoapp.views.exam_result1, name='exam_result1'),
    path('exam_result', infoapp.views.exam_result, name='exam_result'),
    path('delete_ex_re/<id>', infoapp.views.delete_ex_re, name='delete_ex_re'),
    path('delete_test', infoapp.views.delete_test, name='delete_test'),
    path('delete_test1/<id>', infoapp.views.delete_test1, name='delete_test1'),
    path('upl_cer', infoapp.views.upl_cer, name='upl_cer'),
    path('delete_test1/<id>', infoapp.views.delete_test1, name='delete_test1'),
    path('do_cer', infoapp.views.do_cer, name='do_cer'),
    path('del_cer', infoapp.views.del_cer, name='del_cer'),
    path('delete_cert/<id>', infoapp.views.delete_cert, name='delete_cert'),
    path('feedback', infoapp.views.feedback, name='feedback'),
    path('feedbak', infoapp.views.feedbak, name='feedbak'),
    path('delete_feedback/<id>', infoapp.views.delete_feedback, name='delete_feedback'),
    path('subject_ad', infoapp.views.subject_ad, name='subject_ad'),
    path('edit_subject1/<id>/<idd>/<idt>/<pkm>', infoapp.views.edit_subject1, name='edit_subject1'),
    path('delete_subject1/<id>/<idd>/<idt>/<pkm>', infoapp.views.delete_subject1, name='delete_subject1'),
    path('chapter_ad', infoapp.views.chapter_ad, name='chapter_ad'),
    path('edit_chapter1/<id>/<idd>/<idt>/<idk>/<pkm>', infoapp.views.edit_chapter1, name='edit_chapter1'),
    path('delete_chapter1/<id>/<idd>/<idt>/<idk>', infoapp.views.delete_chapter1, name='delete_chapter1'),
    path('ch_co_ad', infoapp.views.ch_co_ad, name='ch_co_ad'),
    path('edit_content1/<id>', infoapp.views.edit_content1, name='edit_content1'),
    path('delete_content1/<id>', infoapp.views.delete_content1, name='delete_content1'),
    path('atten', infoapp.views.atten, name='atten'),
    path('m_m2', infoapp.views.m_m2, name='m_m2'),
    path('del_msg_student/<id>', infoapp.views.del_msg_student, name='del_msg_student'),
    path('reply_msg_student/<id>', infoapp.views.reply_msg_student, name='reply_msg_student'),
    path('sent_msg_student', infoapp.views.sent_msg_student, name='sent_msg_student'),
    path('m_m1', infoapp.views.m_m1, name='m_m1'),
    path('del_msg_teacher/<id>', infoapp.views.del_msg_teacher, name='del_msg_teacher'),
    path('reply_msg_teacher/<id>', infoapp.views.reply_msg_teacher, name='reply_msg_teacher'),
    path('sent_msg_teacher', infoapp.views.sent_msg_teacher, name='sent_msg_teacher'),
    path('m_m3', infoapp.views.m_m3, name='m_m3'),
    path('del_msg_admin/<id>', infoapp.views.del_msg_admin, name='del_msg_admin'),
    path('reply_msg_admin/<id>', infoapp.views.reply_msg_admin, name='reply_msg_admin'),
    path('sent_msg_admin', infoapp.views.sent_msg_admin, name='sent_msg_admin'),
    path('g_m', infoapp.views.g_m, name='g_m'),
    path('delete_g_msg/<id>', infoapp.views.delete_g_msg, name='delete_g_msg'),
    path('abb', infoapp.views.abb, name='abb'),
    path('block', infoapp.views.block, name='block'),
    path('blocks/<id>', infoapp.views.blocks, name='blocks'),
    path('blocks1/<id>', infoapp.views.blocks1, name='blocks1'),
    path('allows/<id>', infoapp.views.allows, name='allows'),
    path('allows1/<id>', infoapp.views.allows1, name='allows1'),
    path('courses', infoapp.views.courses, name='courses'),











]
