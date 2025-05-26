    !��������
    module global
      implicit none
      real, allocatable :: ev(:,:)    !��ά�ɱ����飬�洢����ֵ
      real, allocatable :: kp(:,:)    !��ά�ɱ�����
      real, dimension(3) ::k_0,d      
      character(len=32) :: line, filename = "EIGENVAL"
      integer :: i, n, j
      real :: dk
      logical alive
    end module
    !������
    program band
    use global
    !��ѯ�Ƿ����EIGENVAL�ļ�
    inquire(file=filename,exist=alive)
    if(alive)then
        write(*,*)"The required documents are ready!"
    else
        write(*,*)filename,"doesn't exist."
    end if
    !��ȡEIGNVAL�ļ���������band.dat�ļ�
    open(unit = 10, file = 'EIGENVAL', status = 'old')
    open(unit = 11,file = 'band.dat')
    !ͨ��ѭ������ǰ���е����ݶ�ȡ������
    do n = 1,5
        read(10,'(A)') line
    end do
    
    !��ȡ�ܴ���k���Լ���Ӧ�ı���ֵ
    read(10,*) none,nkp,nbands  
    !write(*,*) nkp, nbands
    allocate(ev(nkp,nbands))   !Ϊ����ev�����ڴ�ռ䣬ʹ���СΪ��nkp,nbands��
    allocate(kp(nkp,3))        !Ϊ����kp�����ڴ�ռ䣬ʹ���СΪ��nkp,3��
        do i = 1,nkp
            read(10,*)         !��ȡ���в�����
            read(10,*) (kp(i,j),j = 1,3),weight  !����i��k�����������洢��kp�У�Ȩ�ش洢��weight��
            do j = 1,nbands
                read(10,*) m,ev(i,j)   !������Լ�����ֵ�洢�ڱ���m��ev(i,j)��
            end do
        end do
!�����ܴ��Ĳ�ʸ֮��ľ���
    do j = 1,nbands                  !����ÿ���ܴ�
        dk = 0                       !������dk��ʼ��Ϊ0
        do i = 1,nkp                 
            if (i.eq.1) then        
                k_0 = kp(i,:)        !��ʼ������k_0
            end if
            d = kp(i,:) - k_0        !���㵱ǰ��ʸk(i,:)��ǰһ����ʸk_0֮��Ĳ�ֵ����������洢������b��
            dk = dk + sqrt(dot_product(d,d))  !���㵱ǰ��ʸk(i,:)��ǰһ����ʸk_0֮��ľ��룬���ۼӵ�����dk�С�����ʹ���������ĵ�����������
                write(11,*)dk,ev(i,j)  !��dk�Լ���Ӧ�ı���ֵ�����band.dat�ļ���
            k_0 = kp(i,:)             !���±���k_0
        end do
        write(11,*)
    end do
    write(*,*) "File output successful!"
    stop
    end program band